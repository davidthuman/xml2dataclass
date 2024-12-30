"""  """

### Imports ###

# Standard Library

import unittest
import xml.etree.ElementTree as ET
import difflib

# Internal Libraries

from xml2dataclass.main import generate_py_file_str, to_data_classes


class CountryDataTestCase(unittest.TestCase):
    
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
            
            