# CandidateCheck

Author: Ryan Craft, Engineering and Physics Undergraduate, Curtin University (Bentley Campus).

Date: 20th July 2021


###################
Overview
###################

CandidateCheck is a repository storing python programs and (possibly) bash scripts aimed at assisting in finding possible new Pulsar candidates with the
Murchison Widefield Array PFD data files. 
The repository borrows code from scienceguyrob/PulsarFeatureLab (https://github.com/scienceguyrob/PulsarFeatureLab) to extract the relevent information.
Subsequent code developed should be designed with the intention of representing the relevent data from the PFD files such that it narrows or quickens the search
for new candidates. 

###################
Requirements
###################

Python 3 or later
Matplotlib
SciPy
Numpy

###################
Use
###################

.... TBC

Author: Ryan Craft, Engineering and Physics Undergraduate, Curtin University (Bentley Campus).

Date: 20th July 2021

################### Overview ###################

CandidateCheck is a repository storing python programs and (possibly) bash scripts aimed at assisting in finding possible new Pulsar candidates with the Murchison Widefield Array PFD data files. 
The repository borrows code from scienceguyrob/PulsarFeatureLab (https://github.com/scienceguyrob/PulsarFeatureLab) to extract the relevent information. 
Subsequent code developed should be designed with the intention of representing the relevent data from the PFD files such that it narrows or quickens the search for new candidates.

################### Requirements ###################

Python 3 or later Matplotlib

################### Use ###################

Main.py:

Located in the Src folder.

Uses PFDFile.py to extract relevent data from user supplied PFD files and output them to a user defined folder.

HOW TO USE:

1. Enter the path of the folder containing the PFD files.
2. Enter the path of the output folder, the folder you want the processed CSV files to go to or
   press enter to generate a default output folder.
3. A plot with DM's vs Periods of the candidates will appear, a CSV file with the extracted data will be generated, named by date&time
   and placed in the output directory. 



