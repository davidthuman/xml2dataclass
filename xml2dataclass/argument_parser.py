""" Module for parsing and resolving the command arguments  """

import sys
import argparse
from dataclasses import dataclass
from enum import Enum


class Out(Enum):
    """ Location of where the output data should be routeds """
    FILE_PATH = 0
    STDOUT = 1


@dataclass
class ArgumentData:
    """ Parsed and resolved data from command arguments """
    args: argparse.Namespace
    xml: str
    out: Out


def arguments() -> ArgumentData:
    """ Returns command arguments data

    Returns:
        ArgumentData: Parsed and resolved argument data
    """

    parser = argparse.ArgumentParser(
        description='xml2dataclass - Code Gen to convert XML structure into Python Dataclasses'
    )

    parser.add_argument(
        'xml',
        nargs='?',
        default=None,
        help='xml input to convert'
    )

    parser.add_argument(
        '-f', '--file',
        type=argparse.FileType('r'),
        help='file path to xml file'
    )

    parser.add_argument(
        '-o', '--output',
        type=argparse.FileType('w'),
        help='file path to output python file'
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='verbose logging'
    )

    args = parser.parse_args()

    xml = ''

    if args.file:
        xml = args.file.read()
    elif args.xml is None:
        if not sys.stdin.isatty():
            xml = sys.stdin.read().strip()
        else:
            parser.error('xml is required, or file must be specified')
    else:
        xml = args.xml

    if args.output:
        out = Out.FILE_PATH
    else:
        out = Out.STDOUT

    data = ArgumentData(args, xml, out)

    return data
