"""  """

### Imports ###

# Standard Library

import unittest
import xml.etree.ElementTree as ET
import difflib
import os
import subprocess

# Internal Libraries

from xml2dataclass.main import generate_py_file_str, to_data_classes


class CountryDataTestCase(unittest.TestCase):
    """ Test class for unit tests on 'country_data' """

    def setUp(self):
        self.root = ET.parse("tests/xml/country_data.xml").getroot()

    def test_output_country_data(self):

        with open("tests/py/country_data.py", "r", encoding="utf-8") as f:

            expected = f.read()
            actual = generate_py_file_str(
                to_data_classes(
                    self.root
                )
            )

            self.assertEqual(
                first=expected,
                second=actual,
                msg=''.join(
                    difflib.ndiff(
                        expected.splitlines(keepends=True),
                        actual.splitlines(keepends=True)
                    )
                )
            )
            
class SenateVoteMenuTestCase(unittest.TestCase):
    """ Test class for unit tests on 'senate_vote_menu' data """
    
    def setUp(self):
        self.root = ET.parse("tests/xml/senate_vote_menu.xml").getroot()
    
    def test_output_senate_vote_menu(self):
        
        with open("tests/py/senate_vote_menu.py", "r", encoding="utf-8") as f:
            
            expected = f.read()
            actual = generate_py_file_str(
                to_data_classes(
                    self.root
                )
            )
            
            self.assertEqual(
                first=expected,
                second=actual,
                msg=''.join(
                    difflib.ndiff(
                        expected.splitlines(keepends=True),
                        actual.splitlines(keepends=True)
                    )
                )
            )
            
class CliTestCase(unittest.TestCase):
    """ Test class for CLI testing """

    def test_position_input_stdout_output(self):
        """ Testing CLI using positional XML input and
            stdout output
        """

        completed_process = subprocess.run(
            [
                'python',
                '-m',
                'xml2dataclass',
                '<?xml version="1.0"?><data/>',
                # '--verbose',
            ],
            capture_output=True,
            check=False
        )

        self.assertEqual(
            0,
            completed_process.returncode,
            f"\n{completed_process.stderr.decode('utf-8')}",
        )

        expected = '''""" This module was generated from xml2dataclass """

from dataclasses import dataclass

@dataclass
class Data:


'''

        actual = completed_process.stdout.decode('utf-8')

        self.assertEqual(
            expected,
            actual,
            ''.join(
                    difflib.ndiff(
                        expected.splitlines(keepends=True),
                        actual.splitlines(keepends=True)
                    )
                )
        )
