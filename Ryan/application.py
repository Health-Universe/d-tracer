import functions
import streamlit as st

data = st.file_uploader("Choose file to upload:")

if data is not None:
	df = functions.upload(data)
	df_keep = functions.format_col(df)
	df_pairs = functions.pick_pairs(df_keep)
	st.write("Dataset available for use.")
else:
	st.write("Please upload a dataset.")

choices = [
	"What do you want to do?",
	"Show Compound Pairs",
	"Adjust Masses",
	"ID Lipids",
	"Visualize"
]
choice = st.selectbox("Pick One:", choices)

if choice == choices[1]:
	st.write(df_pairs)
else: 
	pass

if choice == choices[2]:
	m1 = st.number_input("Enter first mass adjustment:", 0, 80, 5)
	m2 = st.number_input("Enter second mass adjustment:", 0, 80, 11)
	df_adjusted = mass_adj(df_pairs)
	st.write(df_adjusted)
else:
	pass

if choice == choices[3]:
	# Lipidomics database
	pass
else:
	pass

if choice == choices[4]:
	# Visual of lipids???
	pass
else: 
	pass