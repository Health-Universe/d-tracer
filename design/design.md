# Main user - researcher doing mass spec metabolite tracing experiments. 
A wet lab researcher who is not familiar with computer science needs to analyze mass spec data from a lipid
 metabolite tracing experiment using deuterium labeling.

**Basic features of the tool:**
Given peak list generated from Waters Progenesis software, this tool needs to pick out pairs of metabolites 
that contain deuterium based having a certain mass defect and same rt and ccs, within a certain error tolerance.
Next, the tool needs to adjust the mass of the deuterated metabolites by subtracting the mass of the deuterium
so they can be identified using lipidMaps or liPydomics software. 

**Desired features of the tool:**
The tool should have a GUI to make it easy to use for people without Python experience.
The tool can pick out internal standard peaks given masses and retention times.
The tool can input data directly into liPydomics to make lipid identifications.
The tool can plot relative abancences of different lipid classes once identified.

**Input/Output data**
Input: a peak list with m/z, rt, css, and normalized abundance columns for each sample.
Input 2: The desired mass difference and error tolerance for identifying deuterated lipids. 
Optional Input 3: A list of standard m/z and rt values.
Output 1: a subset of the peak list containing pairs of deuterated metabolites.
Output 2: The deuterated subset list with masses adjusted for the deuterium
Output 3: A list of mass adjusted, deuterated lipids that have been identifyed in LiPydomics.

**Tools used**
Use Pandas to organize input data as a dataframe and maintain organization throughout analysis.
Use NumPy to complete calculations (mass adjustment)
Use StreamLit to package everything into a GUI and ask for user input data.

**End Goal:**
A user friendly software to find and idenify deuterium labled lipids from mass spectrometry lipidomics
data.
