import functions
# import id_standards
# import identification
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

n_samples = st.number_input("Enter number of samples:", 0, 100, 10)
df_keep = functions.format_col(df, n_samples)

a = st.number_input("Enter first mass adjustment:", 0, 80, 5)
b = st.number_input("Enter second mass adjustment:", 0, 80, 11)
if b < a:
	st.warning("Second mass must be larger than the first")
	st.stop()

if st.checkbox("Analyze", help="Click to run pair picking algorithm and adjust masses"):
	start = time.time()
	idxs, pairs = functions.pick_pairs(df_keep, a, b)
	df_adjusted = functions.mass_adj(idxs, df_keep, a, b)
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
	st.dataframe(df_adjusted)

	st.download_button(
		label="export to csv",
		data=df_adjusted.to_csv(index=False), 
		file_name="tempfile.csv"
		)

if choice == choices[2]:
	# match lipids to standards
	st.markdown("## Choose standards file to upload")
	df_standard_keep = st.file_uploader("")
	#standards = id_standards(df_keep, df_standard_keep)

	st.download_button(
		label="export to csv",
		data=standard_output.to_csv(index=False),
		file_name="standards.csv"
		)

if choice == choices[3]:
	# match standards to LiPydomics
	lipid_ids = functions.lipid_id(df_adjusted, "output.xlsx")
	st.write(lipid_ids)

	# st.download_button(
	# 	label="export to excel",
	# 	data=lipid_ids,
	# 	file_name="output.xlsx"
	# 	)