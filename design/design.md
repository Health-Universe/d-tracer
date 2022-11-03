##Main user - researcher doing mass spec metabolite tracing experiments. 
A wet lab researcher who is not familiar with computer science needs to analyze mass spec data from a metabolite tracing experiment using deuterium labeling

What do they want to do with the tool?
Have readily readable data output from mass spec data. Use Jupyter notebook for user friendly output

What needs and desires do they want for the tool?
Needs: To pick deuterated compounds (identification/matching), adjust the mass of labeled compounds for the deuterated compound so they can be identified
Output needs: refined spreadsheet of mass spec data

She needs to be able to adjust the parameters for error tolerance, mass difference, and desired outputs without needing to write python code

Desires: Integration with lipid identification software (lipydomics or lipidmaps)

Output wants: labeled peaks on mass spec

She wants to pick out pairs of labeled metabolites that incorporate 2 different labeled fatty acids and adjust their mass so they can be identified with existing lipidomics databases

Wet lab researcher unfamiliar with computer science wants to find the peaks of the standards he added into his sample and their intensities so he can quantify the other peaks present in the sample. 

What is their skill level? 

Main use case:
A wet lab researcher who is not familiar with computer science needs to analyze mass spec data from a metabolite tracing experiment using deuterium labeling. She wants to pick out pairs of labeled metabolites that incorporate 2 different labeled fatty acids and adjust their mass so they can be identified with existing lipidomics databases. She needs to be able to adjust the parameters for error tolerance, mass difference, and desired outputs without needing to write python code. 

Additional use case:
Wet lab researcher unfamiliar with computer science wants to find the peaks of the standards he added into his sample and their intensities so he can quantify the other peaks present in the sample. 

Additional use case: find oxidized species (mass +16, 22, etc)

Visualization: Once lipid are identified, plot their distribution using standard intensities for each class of lipids, structures ??

Use streamlit to organize interface 

Information provided: Peak list with m/z, retention time, ccs (optional), intensities (csv file)
asks you what parameters you are looking for 
mass, RT, CCS, intensity above a given threshold
runs through peak list and identifies matching compounds (converts to dataframe)
asks which output you want (csv or xlsx)
list of matches with respective intensities
list of matches with masses adjusted for deuterium
if case 2, adjusts masses of matches by subtracting 5 or 11 depending on which is incorporated (dataframe)
