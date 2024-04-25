"""Test case for pick_pairs function"""

import functions as fn
import numpy as np
import pandas as pd
import pathlib
import unittest

from collections import Counter

my_data_path = pathlib.Path(__file__).parents[2].joinpath("examples/example_input.csv")

test_data = pd.read_csv(my_data_path, header=2)

formatted_data = fn.format_col(test_data, 6)

# in the form of nx2 np array of unique mass values
true_pairs = [[978.6213752, 972.5837655],
       [976.6035114, 970.5633508],
       [949.6497534, 943.6137902],
       [924.6491739, 918.6112064],
       [922.6331353, 916.5968354],
       [905.6895514, 899.652542 ],
       [896.759428 , 890.7209797],
       [896.6183362, 890.5814109],
       [894.6029557, 888.5667271],
       [894.6027743, 888.5646863],
       [882.6029416, 876.5672706],
       [877.6611081, 871.6239716],
       [874.6422771, 868.6061886],
       [861.6305583, 855.593193 ],
       [839.640121 , 833.6022407],
       [808.598483 , 802.5765976],
       [805.639452 , 799.6012036],
       [803.6240684, 797.586861 ],
       [777.6085929, 771.5711204],
       [761.6128061, 755.5739202]]

class TestPairs(unittest.TestCase):
    """Use the unit test class to create tests cases for pick_pairs"""

    def test_smoke(self):
        """see if fcn runs"""
        fn.pick_pairs(formatted_data, 5, 11)

    def test_edge1(self):
        """Ensures number of pairs is correct before checking the values"""
        idx_pairs, masses = fn.pick_pairs(formatted_data, 5, 11)
        self.assertEqual(len(masses), len(true_pairs))

    def test_oneshot(self):
        """Loops through true pairs for each calculated pair and looks at whether
        the pairs are the same or not. The loop creates a list of T/F values for
        each pair in the calculated list."""
        idx_pairs, masses = fn.pick_pairs(formatted_data, 5, 11)
        l1 = []
        for tpair in true_pairs:
            for pair in masses:
                l2 = []
                res = np.isclose(pair, tpair,rtol=1e-5)
                l2.append(res)
                if np.any(l2):
                    break
                else:
                    continue
            l1.append(np.any(l2))
        self.assertNotIn(False, l1)
    
    # test for 
    
    
