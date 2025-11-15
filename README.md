# xml2dataclass

`xml2dataclass` is a CLI that generates Python [dataclass](https://docs.python.org/3/library/dataclasses.html) objects from XML.

## Usage

```
usage: xml2dataclass [-h] [-f FILE] [-o OUTPUT] [--verbose] [xml]

xml2dataclass - Code Gen to convert XML structure into Python Dataclasses

positional arguments:
  xml                   xml input to convert

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  file path to xml file
  -o OUTPUT, --output OUTPUT
                        file path to output python file
  --verbose             verbose logging
```

The XML structure can be given to the command by either using the `xml` positional argument, specifying a file path with the `--file` argument, piping the XML structure through stdin

```
$ echo '<?xml version="1.0"?><data/>' | xml2dataclass
""" This module was generated from xml2dataclass """

from dataclasses import dataclass

@dataclass
class Data:


```

## Tests

To run the test suite, you can run the command

```sh
make test
```
