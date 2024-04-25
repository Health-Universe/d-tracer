"""tests for mass adjustment function in functions.py"""

import unittest
import unittest.mock as mock
import numpy as np
import functions
import pathlib
import pandas as pd
import sys
 
my_data_path = pathlib.Path(__file__).parents[2].joinpath("examples/example_input.csv")

test_data = pd.read_csv(my_data_path, header=2)                                 
                                                                                
formatted_data = functions.format_col(test_data, 6) 
 
class TestMassAdjust(unittest.TestCase):
    """
    Test for adjusting the mass
    """
 
    def test_smoke(self):
        """
        smoke test to make sure column function runs
        """
        idx_pairs, masses = functions.pick_pairs(formatted_data, 5, 11) 
        
        functions.mass_adj(idx_pairs, formatted_data, 5, 11) 

    def test_correct_mass(self):
        """
        check if the masses are adjusted properly
        """

        idx_pairs, masses = functions.pick_pairs(formatted_data, 5, 11)                             
        pairs = functions.mass_adj(idx_pairs, formatted_data, 5, 11)
        
        for i in range(len(pairs)):
            if (pairs.iloc[i,1] - pairs.iloc[i,2] == 11*1.0063):
                self.assertTrue(pairs) 
            elif (pairs.iloc[i,1] - pairs.iloc[i,2] == 5*1.0063):
                self.assertTrue(pairs) 

    def test_wrong_mass(self):
        """
        force masses to be incorrect 
        """

        idx_pairs, masses = functions.pick_pairs(formatted_data, 5, 11)                             
        pairs = functions.mass_adj(idx_pairs, formatted_data, 5, 11)

        for i in range(len(pairs)):
            if (pairs.iloc[i,1] - pairs.iloc[i,2] == 3*1.0063):
                self.assertTrue(pairs) 
            else:
                self.assertRaises(ValueError, msg="mass adjustment is wrong")
