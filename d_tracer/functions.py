import numpy as np
import pandas as pd
import streamlit as st
import sys
import time

def upload(file, limit=None):
    """Function for importing csv file and removing top two irrelevant rows.
    Optional 'limit' argument to only input the top [X] number of rows."""
    
    df = pd.read_csv(file,header=2, nrows=limit)
    return df


def format_col(df, samples):
    """Function for reducing dataframe columns to those that are applicable,
    and then sorts the data based on 'Compound' name and resets the indices.
    Inputs are a dataframe and optionally the number of samples being analyzed."""

    col_main = ['Compound',
                'm/z',
                'Retention time (min)',
                'CCS (angstrom^2)']

    col = df.columns.tolist() #create a list of all column names
    stop = 16 + samples
    intensities = col[16:stop] #intensity columns we wish to keep
    
    df_keep = df[col_main + intensities].sort_values(
        by=["Compound"], ascending=False).reset_index(drop=True)
    return df_keep

@st.cache
def pick_pairs(df, a, b):
    """Function for analyzing data and picking out pairs of compounds where the
    RT and CCS match, and the m/z is within the mass-adjustment.
    Inputs are a dataframe and two mass-adjustment components."""

    """Define lists and tolerances of each column to compare with itself"""
    mz = np.array(df['m/z'])
    mz_tol = 1e-4
    rt = np.array(df['Retention time (min)'])
    rt_tol = 1e-3
    ccs = np.array(df['CCS (angstrom^2)'])
    ccs_tol = 1e-3
    D = 1.0063 # Deuterium
    mass_adjust = D*(b - a)

    idxs = [] # Initial list for pairs to be held if they pass the following checks
    """Create nested for loop to compare i with j in each column"""
    for i in range(len(df)):
        for j in range(i+1, len(df)):
            """Define checks for each column"""
            check_rt = np.isclose(rt[i], rt[j], rt_tol)
            if check_rt == True: pass # Move on
            else: continue # Move to next iteration

            check_mz = np.isclose(mz[i], mz[j] + mass_adjust, mz_tol)
            if check_mz == True: pass
            else: continue

            check_ccs = np.isclose(ccs[i], ccs[j], ccs_tol)
            if check_ccs == True: pass
            else: continue
            
            idxs.append([i,j])
            pairs = np.array(idxs)

    return pairs


def mass_adj(pairs, df, m1, m2):
    """Adjusts masses of given dataframe and list of pairs. Pairs must be together,
    with higher mass first. x is the lower value, y is the higher value."""
    D = 1.0063
    df_pairs = df.iloc[pairs.flatten()]
    masses = np.array(df_pairs["m/z"]).reshape((len(pairs), 2))
    masses[:, 0] -= m2*D
    masses[:, 1] -= m1*D

    df_pairs.insert(2, "m/z_adj", masses.flatten().tolist())
    return df_pairs

