""" This module contains types """

from dataclasses import dataclass

### Data Structures ###

@dataclass
class FieldLite:
    """ Class for holding information to generate a Python dataclass field """

    name: str
    type_hint: str

    def to_py_str(self):
        """ Return a Python syntax string of the dataclass field

        Returns:
            str: Python syntax of the dataclass field
        """
        return f"{self.name}: {self.type_hint}"

@dataclass
class DataClass:
    """ Class for holding information to generate a Python dataclass """

    name: str
    attributes: list[FieldLite]
    fields: list[FieldLite]

    def to_py_str(self):
        """ Returns a Python syntax string of the dataclass
        
        Returns:
            str: Python syntax of the dataclass
        """

        fields_py_str = ""

        for field in [*self.attributes, *self.fields]:

            fields_py_str += "    " + field.to_py_str() + "\n"

        py_str = f"""\
@dataclass
class {self.name}:

{fields_py_str}
"""
        return py_str
