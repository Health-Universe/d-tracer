import functions
import streamlit as st

data = st.file_uploader("Choose file to upload:")

if data is not None:
	df = functions.upload(data)
	df_keep = functions.format_col(df)
	df_pairs = functions.pick_pairs(df_keep)
	
	st.write(df_pairs)




else:
	st.write("Please upload a dataset.")