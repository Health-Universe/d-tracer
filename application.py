"""This module calls upon the functions module to write a web application
to streamlit. It starts by uploading a dataset from the mass spectronomy machine.
This dataset is formatted to remove unnecessary columns, given the number of
samples that were analyzed. The application gives the user a choice to either
look at the pairs of lipids in the dataset, or to search for standards within the dataset.
If the pairs radio button is chosen, it runs the lengthy pair_picking algorithm which can
take an average of 5 min. Afterwards, the user has the option to view the data of the pairs
and export, or compare the pairs with the LiPydomics database."""

from d_tracer import functions
# import identification
import pandas as pd
import streamlit as st
import time


# """Upload the csv datafile from the mass spec machine."""
data = st.file_uploader("Choose file to upload:")

# """If nothing is yet uploaded, do not show anything further."""
if data is None:
	st.warning("Please upload a dataset.")
	st.stop()

# """Load the data to a pandas dataframe."""
df = functions.upload(data)
st.success("Dataset available for use")
time.sleep(.5)

# """Define number of samples tested and trim unnecessary columns,
# creating a new dataframe."""
n_samples = st.number_input("Enter number of samples:", 0, 100, 10)
df_keep = functions.format_col(df, n_samples)

# """Display two paths for continuing in the app. Finding standards
# does not execute the lengthy pair picking algorithm."""
choice_a = st.radio("What would you like to do?",
					("Find pairs", "Find Standards"))


if choice_a == "Find Standards":
	"""Define the standards the user is looking for and find it in the dataset."""
	mz_standard = st.number_input("mz_standard", value=480.30833, format="%0.5f")
	rt_standard = st.number_input("rt_standard", value=7.60298, format="%0.5f")

	standards = functions.id_standards(df_keep, mz_standard, rt_standard)
	st.dataframe(standards)
	st.stop()


else: pass # This else statement encapsulates pair picking

# """Define masses to be adjusted."""
m1 = st.number_input("Enter first mass adjustment:", 0, 80, 5)
m2 = st.number_input("Enter second mass adjustment:", 0, 80, 11)
if m2 < m1:
	st.warning("Second mass must be larger than the first")
	st.stop()

# """Check the box to execute the pair picking and mass-adjustment algorithm and cache
#  the result. The 'st.button' feature would not work in this context because it does 
#  not remain 'True' after the button is pressed."""
if st.checkbox("Analyze", help="Click to run pair picking algorithm and adjust masses"):
	start = time.time()
	idxs, pairs = functions.pick_pairs(df_keep, m1, m2)
	df_adjusted = functions.mass_adj(idxs, df_keep, m1, m2)
	# st.progress()
	end = time.time()
	st.success(str(pairs.shape[0]) + " pairs found | Runtime = " + str(round(end-start, 2)) + " seconds")
else: st.stop()

# """Define choices of data for the user to view."""
choices = [
	"What do you want to see?",
	"Show mass-adjusted data of pairs",
	"Identify Lipids"
	]
choice_b = st.selectbox("Pick One:", choices)

if choice_b == choices[1]:
	st.dataframe(df_adjusted)

	st.download_button(
		label="Export to CSV",
		data=df_adjusted.to_csv(index=False), 
		file_name="tempfile.csv"
		)

if choice_b == choices[2]:
	temp_data = st.file_uploader("Choose file to upload again:")
	csv_data = pd.read_csv(temp_data)
	if temp_data is None:
		st.stop()
	lipid_ids = functions.lipid_id(csv_data)
	st.write('Identification Complete, ID saved to data/output_data')

	#st.download_button(
		#label="Export to CSV",
		#ata=df_adjusted.to_csv(index=False), 
		#file_name="tempfile.csv"
		#)