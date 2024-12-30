"""  """

import argparse

def arguments() -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        description='xml2dataclass - Code Gen to convert XML structure into Python Dataclasses'
    )

    parser.add_argument(
        '--file', 
        type=str,
        help='file path to xml file'
    )

    parser.add_argument(
        '--output', 
        type=str,
        help='file path to output python file'
    )

    args = parser.parse_args()
    
    return args