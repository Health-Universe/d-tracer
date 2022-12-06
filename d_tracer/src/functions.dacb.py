import pandas as pd
import numpy as np

def upload(file):
    """define fcn for receiving file in a pandas dataframe"""
    df = pd.read_csv(file,header=2)
    return df 

def format_col(df):
    """define fcn for reducing columns"""
    col = df.columns.tolist() #create a list of all column names
    main = [0,2,4,5] #Index of main columns we wish to keep and compare
    stop = col.index([col for col in df.columns if '.1' in col][0]) #index of duplicate columns we don't need
    intensities = col[16:stop] #intensity columns we wish to keep
    col_main = [] #Column names of kept columns
    for i in main:
        col_main.append(col[i])
    
    # Create new filtered dataframe of important columns
    df_keep = df[col_main + intensities]
    return df_keep 

# fcn for picking compound pairs
def pick_pairs(df, m1, m2):
    """Define lists and tolerances of each column to compare with itself"""

    # note using numpy arrays because they are faster than python lists
    mz = np.array(df['m/z'])
    mz_tol = 1e-4
    rt = np.array(df['Retention time (min)'])
    rt_tol = 1e-3
    ccs = np.array(df['CCS (angstrom^2)'])
    ccs_tol = 1e-3
    D = 1.0063

    # initialize a list for indexes to be held for each pair of matched values
    idxs = []
    # nested for loop to compare i with j in each column
    mass_adjust = m1*D - m2*D
    for i in range(len(df)):
        for j in range(i+1, len(df)):
            # Define checks for each column
            check_mz = np.isclose(mz[i], mz[j] + mass_adjust, mz_tol) \
                         or np.isclose(mz[j], mz[i] + mass_adjust, mz_tol)
            check_rt = np.isclose(rt[i], rt[j], rt_tol)
            check_ccs = np.isclose(ccs[i], ccs[j], ccs_tol)
            
            # Record results of each check (True/False)
            checks = [check_mz, check_rt, check_ccs]

            # If all checks are true, append to list of pairs
            if all(checks):
                idxs.append([i, j])
            else:
                pass

    # we only need to convert this to a numpy list after it is
    # completely constructed
    pairs = np.array(idxs)
    return pairs

def mass_adj(pairs, df, m1, m2):
    """fcn for adjusting masses

    Adjusts masses of given dataframe and list of pairs. Pairs must be together,
    with higher mass first. x is the lower value, y is the higher value."""
    D = 1.0063
    df_pairs = df.iloc[pairs.flatten()]
    masses = np.array(df_pairs["m/z"]).reshape((len(pairs), 2))
    masses[:, 0] -= m2*D
    masses[:, 1] -= m1*D

    df_pairs.insert(2, "m/z_adj", masses.flatten().tolist())
    return df_pairs

