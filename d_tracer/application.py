import functions
import streamlit as st
import time

data = st.file_uploader("Choose file to upload:")

if data is None:
	st.warning("Please upload a dataset.")
	st.stop()

# if st.button("Upload") == False: st.stop()

df = functions.upload(data, 1000)
st.success("Dataset available for use")
time.sleep(1)

n_samples = st.number_input("Enter number of samples:", 0, 100, 0)
df_keep = functions.format_col(df, n_samples)

a = st.number_input("Enter first mass adjustment:", 0, 80, 5)
b = st.number_input("Enter second mass adjustment:", 0, 80, 11)
if b < a:
	st.warning("Second mass must be larger than the first")
	st.stop()

if st.checkbox("Analyze", help="Click to run pair picking algorithm and adjust masses"):
	start = time.time()
	pairs = functions.pick_pairs(df_keep, a, b)
	# st.progress()
	end = time.time()
	st.success(str(pairs.shape[0]) + " pairs found | Runtime = " + str(round(end-start, 2)) + " seconds")
else: st.stop()


choices = [
	"What do you want to do?",
	"Show mass-adjusted data of pairs",
	"Find Standards",
	"Identify Lipids"
	]
choice = st.selectbox("Pick One:", choices)

if choice == choices[1]:
	# pairs = functions.pick_pairs(df_keep, a, b)
	df_adjusted = functions.mass_adj(pairs, df_keep, a, b)
	st.dataframe(df_adjusted)

if choice == choices[2]:
	# match lipids to standards
	pass

if choice == choices[3]:
	# match standards to LiPydomics
	pass