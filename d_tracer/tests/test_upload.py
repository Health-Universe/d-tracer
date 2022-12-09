"""test for upload function"""

import unittest
import numpy as np
import functions
import pathlib

my_data_path = pathlib.Path(__file__).parents[2].joinpath("examples/example_input.csv")
wrong_data = pathlib.Path(__file__).parents[2].joinpath("examples/example_wrong_input.csv")


class TestUpload(unittest.TestCase):
    """
    Test for upload function
    """
    

    def test_smoke(self):
        """
        smoke test to make sure upload function runs
        """
        functions.upload(my_data_path, limit=None)

    def test_correct_file_type(self):
        """
        this test should show that space delimited files are incorrect
        """
        with self.assertRaises(ValueError):
            functions.upload(wrong_data, limit=None)
            print("Incorrect csv format. please make sure it is comma separated")   

        
