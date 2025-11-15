""" This module was generated from xml2dataclass """

from dataclasses import dataclass

@dataclass
class For:

    continue_: str
    class_: str
    def_: str

@dataclass
class Return:

    if_: str
    else_: str
    for_: For

@dataclass
class Test:

    returns: list[Return]

