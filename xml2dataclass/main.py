"""  """

### Imports ###

# Standard Library

import xml.etree.ElementTree as ET
import sys
import logging
from collections.abc import Callable

# Internal Libraries

from xml2dataclass.types import DataClass, FieldLite
from xml2dataclass.argument_parser import arguments, Out

### Helper ###

def to_class_name(name: str) -> str:

    for char in ["-", ".", ":"]:
        name = name.replace(char, "_")

    words = name.split("_")

    return "".join(map(lambda word: word[0].upper() + word[1:], words))


def parse_element(element: ET.Element, data_classes: list[DataClass]):

    # parse children elements

    child_count = {}

    for child in element:

        if child.tag not in child_count:
            child_count.update({child.tag: 1})
        else:
            child_count.update({child.tag: child_count.get(child.tag) + 1})

    # Determine type of child element
    # - if no children element -> basic type
    # - if has attributes -> needs dataclass
    # - if has children element -> needs dataclass

    child_needs_dataclass = {}

    for key in child_count.keys():

        # Check all instances of child element, in case the parent element has different structured child elements

        for child in element.findall(key):

            has_attributes = len(child.attrib) > 0
            has_children = len(child) > 0

            needs_dataclass = has_attributes or has_children

            if key not in child_needs_dataclass:
                child_needs_dataclass.update({key: needs_dataclass})
            else:
                child_needs_dataclass.update(
                    {key: child_needs_dataclass.get(key) or needs_dataclass})

    # Create element's

    # if child element has more than 1 instance, field on parent element will be a list of the child element type

    attributes = []
    fields = []

    for attribute_name in element.attrib.keys():

        attributes.append(FieldLite(attribute_name, "str"))

    for tag, needs_dataclass in child_needs_dataclass.items():

        # Field Name
        if child_count.get(tag) == 1:
            field_name = tag
        else:
            field_name = tag + "s"

        # Field Type
        if not needs_dataclass:
            field_type = "str"
        else:
            sub_data_class = parse_element(element.find(tag), data_classes)
            tag_type = sub_data_class.name
            field_type = f"{tag_type}"

        if child_count.get(tag) > 1:
            field_type = f"list[{field_type}]"

        fields.append(FieldLite(field_name, field_type))

    data_class = DataClass(to_class_name(element.tag), attributes, fields)

    data_classes.append(data_class)

    return data_class


def to_data_classes(root: ET.Element) -> list[DataClass]:

    data_classes: list[DataClass] = []

    parse_element(root, data_classes)

    return data_classes


def generate_py_file_str(data_classes: list[DataClass]) -> str:
    
    py_file_str = ""        
    
    def write(s: str):
        nonlocal py_file_str
        py_file_str += s
    
    write_py(write, data_classes)
    
    return py_file_str

def write_py(write: Callable[[str], int], dataclasses: list[DataClass]):
    """ Writes the given dataclasses using the given write function """
    
    write('""" This module was generated from xml2dataclass """\n')
    write("\n")
    write("from dataclasses import dataclass\n")
    write("\n")
    for dc in dataclasses:
        write(dc.to_py_str())


def main():

    arg_data = arguments()

    if arg_data.args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    logger = logging.getLogger(__name__)

    logger.debug('XML: %s', arg_data.xml)

    root = ET.fromstring(arg_data.xml)

    dcs = to_data_classes(root)

    match (arg_data.out):

        case Out.FILE_PATH:
            with open(arg_data.args.output, "a", encoding="utf-8") as f:
                write_py(f.write, dcs)

        case Out.STDOUT:
            write_py(sys.stdout.write, dcs)
