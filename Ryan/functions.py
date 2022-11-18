import pandas as pd
import numpy as np
import streamlit as st

'''define fcn for receiving file in a pandas dataframe'''
def upload(file):
	df = pd.read_csv(file,header=2) 
	return df 

'''define fcn for reducing columns'''
def reduce_col(df):
    col = df.columns.tolist() #create a list of all column names
    main = [0,2,4,5] #Index of main columns we wish to keep and compare
    stop = col.index([col for col in df.columns if '.1' in col][0]) #index of duplicate columns we don't need
    intensities = col[16:stop] #intensity columns we wish to keep
    col_main = [] #Column names of kept columns
    for i in main:
        col_main.append(col[i])
    '''Create new filtered dataframe of important columns'''
    df_keep = df[col_main+intensities][:100]
    return df_keep 

'''fcn for picking compound pairs'''
def pick_pairs():
    pass

'''fcn for adjusting masses'''
def mass_adj(df,a,b):
    pass

