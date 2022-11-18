import functions
import streamlit as st

data = st.file_uploader("Choose file to upload:")

if data is not None:
	df = functions.upload(data)
	functions.reduce_col(df)


