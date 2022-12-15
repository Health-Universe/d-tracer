"""tests for mass adjustment function in functions.py"""

import unittest
import unittest.mock as mock
import numpy as np
import functions
import pathlib
import pandas as pd
import sys
 
my_data_path = pathlib.Path(__file__).parents[2].joinpath("examples/example_input.csv")
 
class TestMassAdjust(unittest.TestCase):
    """
    Test for adjusting the mass
    """
 
    def test_smoke(self):
        """
        smoke test to make sure column function runs
        """
        # functions.mass_adj(pairs,df, a, b)
        pass
 
