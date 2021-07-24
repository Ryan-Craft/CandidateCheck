# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 16:53:58 2021

@author: Ryan Craft

Descripton:
    
    Trying to make a simpler version of the "PulsarFeatureLab.py" program.
    
    Arguments consisting of only type, name and Directory.
    
    **Should be able to write the desired features to CSV folders??**


PSEUDO CODE:
    
    I need to have the Drive Path and candidate name, cand name is going to be the same as the drive path.
    This needs to be defined by user input (Exception handling last)

    Path = string(input("Input file path: "))

    The I can use Utilities.py to check that the path exists:
    Utilities.fileExists(Path)

    Which will throw an error when the path does not exist

"""


######
# Imports
#
######

import Utilities as Util
import Candidate as cand
import os
import glob



######
# Declare Variables
#
######

Bool1 = False
Path = ""
CandidateList = []
CandidateNameList = []
CandidateDataList = []
######
# User Inputs
# --- Input directory PATH where pfd files are located
# --- Output directory  PATH where csv files are to be created, written to and saved
# --- Need some sort of file path checking system so that there cannot be and IOError
# Additions required:
# --- Needs to prompt the user to select / create a new folder for csv file output later on
######

print("\n###################### Pulsar Candidate Check ######################\n")


# Below input loop stops people from crashing the program by typing incorrect PATH into the program, also allows them to exit if they change their mind
# Big thanks to the Utlities.py program which already contains file path checking functions, !!!!!!!!!!!!!!!auth cred!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

while Bool1 == False:

    Path = str(input("Insert file PATH to the folder containing PFD candidates or enter 'Exit' to exit: \n"))
    PathObj = Util.Utilities(Path)
    Bool1 = PathObj.dirExists(Path)

    if Path == "Exit": 
        print("\n### Program Exit by User ###\n")
        os._exit(0)
    
    if Bool1 == False and Path !="Exit":
        print("\nSpecified PATH was not found\n")

######
# File Reading loop, creating arrays for holding the object data (appending them to a list for later) using candidate.py
# --- Loop which navigates to the file path and then creates an object for each file in the folder
# --- loops appends each candidate object to a list.
# --- For each object in the list, the array associated with its parameters is written into a unique csv file
# --- we dont want it to make plots cos it will slow everythin down (plots are disabled in PFDfeatureExtractor and FeatureExtractor)
######

"""
What I want to happen here is for the program to take the file given in the path variable and do the candidate object operation on each of the
files in the folder until it terminates. 

"""
#Below code modified from StackOverflow: https://stackoverflow.com/questions/18262293/how-to-open-every-file-in-a-folder

CandidatePath = Path
for filename in glob.glob(os.path.join(CandidatePath,  "*.pfd")):
  with open(filename, 'rb') as f:
    CandidateName = filename
    CandidateNameList.append(CandidateName)
    NewCand = cand.Candidate(CandidateName, CandidateName)
    CandidateList.append(NewCand)
    CandidateData = NewCand.getFeatures(3,3,True)
    CandidateDataList.append(CandidateData)

print(CandidateNameList)
print(CandidateDataList)

    