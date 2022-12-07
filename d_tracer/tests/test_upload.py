"""test for upload function"""

import unittest
import numpy as np
import functions
import pathlib

my_data_path = pathlib.Path(__file__).parents[2].joinpath("examples/example_input.csv")

class TestUpload(unittest.TestCase):
    """
    Test for upload function
    """
    

    def test_smoke(self):
        """
        smoke test to make sure upload function runs
        """
        functions.upload(my_data_path, limit=None)

    def test_file_type(self):
        """
        testing to make sure a csv file is uploaded
        """
        try:
            functions.upload(my_data_path, limit=None) 
        except IOError:
            print("CANNOT OPEN FILE. INCORRECT FILE FORMATTING!")
        
