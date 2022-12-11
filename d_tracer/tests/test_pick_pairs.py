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

# in the form of nx2 np array of compound names
true_pairs = [['6.36_877.6611m/z', '6.36_871.6240m/z'],
       ['5.17_803.6241m/z', '5.17_797.5869m/z'],
       ['5.17_777.6086m/z', '5.17_771.5711m/z'],
       ['5.05_761.6128m/z', '5.05_755.5739m/z'],
       ['3.41_924.6492m/z', '3.41_918.6112m/z'],
       ['3.41_896.7594m/z', '3.41_890.7210m/z'],
       ['3.38_978.6214m/z', '3.38_972.5838m/z'],
       ['1.71_808.5985m/z', '1.71_802.5766m/z'],
       ['1.02_976.6035m/z', '1.02_970.5634m/z'],
       ['0.90_861.6306m/z', '0.90_855.5932m/z'],
       ['0.90_839.6401m/z', '0.90_833.6022m/z']]

class TestPairs(unittest.TestCase):
    """Use the unit test class to create tests cases for pick_pairs"""

    def test_smoke(self):
        """see if fcn runs"""
        fn.pick_pairs(formatted_data, 5, 11)

    def test_oneshot(self):
        """Loops through true pairs for each calculated pair and looks at whether
        the pairs are the same or not. The loop creates a list of T/F values for
        each pair in the calculated list."""
        idx_pairs, compound_pairs = fn.pick_pairs(formatted_data, 5, 11)
        l1 = []
        for pair in compound_pairs:
            for tpair in true_pairs:
                res = np.any(Counter(pair)==Counter(tpair))
                if res == True: 
                    l1.append(res)
                    break
                elif tpair == true_pairs[-1]:
                    l1.append(res)
        self.assertNotIn(False, l1)
    
    # test for 
    
    def test_edge(self):
        pass
