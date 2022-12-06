"""all unit tests for code"""

import numpy as np
import pandas as pd
import unittest
from scripts import functions as fn

"""testing input files and formatting"""

"""testing mass parameters"""

"""testing pairs module"""

test_data = pd.read_csv('data/formatted_data.csv')
# current test_data is only the first 200 rows

true_pairs = np.array([
            [  0, 188],
            [ 14,  45],
            [ 16,  15],
            [ 20,  18],
            [ 25, 150],
            [ 28,  24],
            [ 35, 104],
            [ 36,  24],
            [ 38,  26],
            [ 41, 135],
            [ 43, 149],
            [ 44,  10],
            [ 54,  75],
            [ 55, 101],
            [ 56,  30],
            [ 57, 172],
            [ 70,   4],
            [ 88, 157],
            [ 92,  90],
            [105,  64],
            [121,  48],
            [138,  67],
            [164, 129],
            [167, 180],
            [191, 198], 
            [199, 136]])


class TestPairs(unittest.TestCase):
    """Use the unit test class to create tests cases for pick_pairs"""

    def test_smoke(self):
        """see if pick pairs function runs"""
        fn.pick_pairs(test_data, 5, 11)

    def test_oneshot(self):
        """See if pairs are accurate"""
        pairs = fn.pick_pairs(test_data, 5, 11)
        # self.assertEqual(pairs.flatten().tolist(), true_pairs.flatten().tolist())
        self.assertIsNone(np.testing.assert_array_equal(pairs, true_pairs))
    
    def test_edge(self):
        pass
