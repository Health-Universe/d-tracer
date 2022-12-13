# D-Tracer
*Noelle Reimers, Ryan Ostrander, Alyson Shoji, Chau Vuong* 

A tool for picking out deuterium labeled compounds from an ion-mobility mass spectrometry peaklist.

## Overview 

D-Tracer is a software to analyze deuterium labeling mass spectrometry data. It is intended for lipidomics data, however can be used for other mass spectrometry datasets. It picks out deuterium-labeling peaks based on input values from the user. This list of labeled peaks can then be mass-adjusted to remove the additional mass of the deuterium label. For lipidomics data, the lipid species can then be identified using integrated [LiPydomics](https://github.com/dylanhross/lipydomics) 
software. Internal standards can be selected from the peak list and structures can be provided for identified lipids. 


## How to use

D-Tracer is available as a user-friendly webpage at [this url](https://nreimers99-d-tracer-d-tracerapplication-hdyn0b.streamlit.app/). It is intended to be accessible for people with limited programming experience. It can also be cloned from the GitHub repository for those comfortable with Python.

Either way you choose to use D-Tracer, it will require some user inputs. The first is a peak list in .csv format. The peak list must have columns for m/z, retention time, and ccs values as well as normalized intensities for 1 or more samples. 

The user can then choose the desired functionality from a drop-down menu. 
* Show mass-adjusted pairs: Pick deuterated species form peak list and return a .xlsx file with the deuterated pairs and their adjusted masses.
* Find Standards: Find internal standards from a list of masses in the peaklist and return a .xlsx file with standards and their intensities in each sample.
* Identify Lipids: Uses integrated LiPydomics software to identify the mass-adjusted deuterated lipid species.

The user will also need to input their number of samples (1-100) and the mass difference for the deuterium labeling. For example, if you were looking for species labeled with D-8, you would enter 0 as the first number and 8 as the second number. if you added both D-5 and D-11, you would enter 5 for the first number and 11 for the second number. These values will be multiplied by the mass difference between deuterium and hydrogen (1.0063) and used to find pairs of peaks that have the same mass once adjusted for the deuterium. The first number must be smaller than the second.

## Repository Structure
```
├── d_tracer
│   ├── __init__.py
│   ├── application.py
│   ├── functions.dacb.py
│   ├── functions.py
│   ├── requirements.txt
│   └── tests
│       ├── __init__.py
│       ├── test_format_col.py
│       ├── test_mass_adjust.py
│       ├── test_pick_pairs.py
│       └── test_upload.py
```
## Dependencies

The identification module of D-Tracer uses an open-source software called [LiPydomics](https://github.com/dylanhross/lipydomics). It can be installed using the command pip install LiPydomics, and will be installed automatically when using the virtual envirnment provided in our environment.yml file. If you are not identifying lipids, LiPydomics is not needed to use D-Tracer.

## Diagram

![Structure of D-Tracer](/doc/dtracer_scheme.png)



