import functions
import streamlit as st
import time

data = st.file_uploader("Choose file to upload:")

if data is None:
	st.write("Please upload a dataset.")
elif st.button("Upload"):
	df = functions.upload(data)
	st.write("Dataset available for use...")

	limit = st.number_input("Set row limit: ", 1, len(df), 100)
	df_keep = functions.format_col(df)[:limit]

	a = st.number_input("Enter first mass adjustment:", 0, 80, 5)
	b = st.number_input("Enter second mass adjustment:", 0, 80, 11)
	if b<a:
		raise ValueError("b must be larger than a")

	if st.button("Find Pairs", help="Click to run pair picking algorithm"):
		start = time.time()
		pairs = functions.pick_pairs(df_keep, a, b)
		end = time.time()
		st.write("Compound Pairs found.")
		st.write("Runtime: ", end-start, "s")

choices = [
	"What do you want to do?",
	"See Full Dataset",
	"Show Compound Pairs",
	"Show Data for Compound Pairs",
	"Adjust Masses of Pairs",
	"ID Lipids",
	"Visualize"
	]
choice = st.selectbox("Pick One:", choices)

if choice == choices[1]:
	st.write(df)

if choice == choices[2]:
	st.write(pairs)

if choice == choices[3]:
	st.write(df_keep[pairs.flatten()])

if choice == choices[4]:
	pairs = functions.pick_pairs(df_keep, a, b)
	df_adjusted = functions.mass_adj(pairs, df_keep, a, b)
	st.write(df_adjusted)

if choice == choices[5]:
	# Lipidomics database
	pass

if choice == choices[6]:
	# Visual of lipids???
	pass