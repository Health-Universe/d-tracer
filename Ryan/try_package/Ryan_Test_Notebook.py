#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import streamlit as st


# # Upload and format data

# In[2]:


data = '../../data/2022_07_13_WTvsKO_allcompounds_neg.csv'
### Need a way for .py file to ask which file to upload
df = pd.read_csv(data,header=2)


# In[54]:


col = df.columns.tolist() #create a list of all column names
main = [0,2,4,5] #Index of main columns we wish to keep and compare
stop = col.index([col for col in df.columns if '.1' in col][0]) #index of duplicate columns we don't need
intensities = col[16:stop] #intensity columns we wish to keep
col_main = [] #Column names of kept columns
for i in main:
    col_main.append(col[i])
'''Create new filtered dataframe of important columns'''
df_keep = df[col_main+intensities][:100]


# # Look for pairs in data and print results

# In[78]:


'''Define lists and tolerances of each column to compare with itself'''
mz = df_keep['m/z']
mz_tol = 1e-4
rt = df_keep['Retention time (min)']
rt_tol = 1e-3
ccs = df_keep['CCS (angstrom^2)']
ccs_tol = 1e-3

'''Initialize a list for indexes to be held for each pair of matched values'''
idxs = []
'''Create nested for loop to compare i with j in each column'''
for i in range(len(df_keep)):
    for j in range(len(df_keep)):
        '''Define checks for each column'''
        check_mz = np.isclose(mz[i], mz[j]+6.02, mz_tol)        
        check_rt = np.isclose(rt[i], rt[j], rt_tol)
        check_ccs = np.isclose(ccs[i], ccs[j], ccs_tol)
        
        '''Record results of each check (True/False)'''
        checks = [check_mz, check_rt, check_ccs]
        
        '''If all checks are true, append to list of pairs'''
        if all(checks) and i!=j:
            idxs.append([i,j])
            pairs = np.array(idxs)
        else:
            pass
print(pairs)

df_pairs = df_keep.iloc[pairs.flatten()]


# # Adjust mass of each pair

# In[79]:


# df_adjusted = df_pairs
# for i in pairs:
#     df_adjusted['m/z'].iloc[i[0]]-=5
#     df_adjusted['m/z'].iloc[i[1]]-=11


# In[ ]:




