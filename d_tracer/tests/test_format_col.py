"""unit test to test functions.format_col"""

import unittest
import unittest.mock as mock
import numpy as np
import functions
import pathlib
import pandas as pd
import sys

my_data_path = pathlib.Path(__file__).parents[2].joinpath("examples/example_input.csv")

class TestColumn(unittest.TestCase):
    """
    Test for upload function
    """

    def test_smoke(self):
        """
        smoke test to make sure column function runs
        """
        df=functions.upload(my_data_path,limit=None)
        functions.format_col(df, 1)

    def test_header_length(self):
        """
        test to check that headers are made correctly and that they have the
        right length
        """
        df=functions.upload(my_data_path,limit=None)
        df_edit=functions.format_col(df, 1)

        message="headers not matching!"

        self.assertEqual(len(df_edit.columns), 5, message) 
        
