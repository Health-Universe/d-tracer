"""
This module takes in the list of mass-adjusted lipids and uses LiPydomics to idenfity them.
It then returns a .xlsx file with the original data in one sheet and the identifications
in the other. The first 3 columns of the input file MUST be m/z, rt, and ccs.
"""

from lipydomics.data import Dataset
from lipydomics.identification import add_feature_ids

def identify_lipids(inputfile, outputfile):
    """
    This function takes in the path and name of desired .csv input file to analyze
    and the path and name of desired .xlsx output file. Input MUST end in .csv and
    output MUST end in .xlsx

    It uses the idetification module of LiPydomics to identify lipid species present
    in the input file. Tolerances for mz, rt, and ccs are set at 0.03, 0.3, and 3.0.
    """
    mz_tol = 0.03
    rt_tol = 0.3
    ccs_tol = 3.0
    tol = [mz_tol, rt_tol, ccs_tol]
    dset = Dataset(inputfile, esi_mode='neg')
    print(dset)
    add_feature_ids(dset, tol, level='any')
    dset.export_xlsx(outputfile)
    print('Identification Complete')

infile = open('../data/test_data/2022_04_22_NEG_RSL3DAAvsCtrl_CSV_mz-d_test_output.csv')
outfile = '../data/output_data/identification_output.xlsx'

identify_lipids(infile, outfile)
