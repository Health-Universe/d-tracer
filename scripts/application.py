import functions
import streamlit as st

data = st.file_uploader("Choose file to upload:")
limit = 100

if data is not None:
	df = functions.upload(data)
	df_keep = functions.format_col(df)#[:limit]
	st.write("Dataset available for use.")

	a = st.number_input("Enter first mass adjustment:", 0, 80, 5)
	b = st.number_input("Enter second mass adjustment:", 0, 80, 11)
	if b<a:
		raise ValueError("b must be larger than a")

else:
	st.write("Please upload a dataset.")

choices = [
	"What do you want to do?",
	"Show Compound Pairs",
	"Adjust Masses of Pairs",
	"ID Lipids",
	"Visualize"
	]
choice = st.selectbox("Pick One:", choices)

if choice == choices[1]:
	df_pairs = functions.pick_pairs(df_keep, a, b)
	st.write(df_pairs)
else: 
	pass

if choice == choices[2]:
	pairs = functions.pick_pairs(df_keep, a, b)
	df_adjusted = functions.mass_adj(pairs, df_keep, a, b)
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