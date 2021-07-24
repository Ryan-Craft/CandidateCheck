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
######
# Declare Variables
#
######
Bool1 = False
Path = ""



######
# User Inputs
# --- Input directory PATH where pfd files are located
# --- Output directory  PATH where csv files are to be created, written to and saved
# --- Need some sort of file path checking system so that there cannot be and IOError
######

print("\n###################### Pulsar Candidate Check ######################\n")


# Below input loop stops people from crashing the program by typing incorrect PATH into the program, also allows them to exit if they change their mind
# Big thanks to the Utlities.py program which already contains file path checking functions, !!!!!!!!!!!!!!!auth cred!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

while Bool1 == False:

    Path = str(input("Insert file PATH to the folder containing PFD candidates or enter 'Exit' to exit: \n"))
    PathObj = Util.Utilities(Path)
    Bool1 = PathObj.fileExists(Path)

    if Path == "Exit": 
        print("\n### Program Exit by User ###\n")
        os._exit(0)
    
    if Bool1 == False and Path !="Exit":
        print("\nSpecified PATH was not found\n")

######
# File Reading loop, creating arrays for holding the object data (appending them to a list for later) using candidate.py
# --- Input directory PATH where pfd files are located
# --- Output directory  PATH where csv files are to be created, written to and saved
# --- Need some sort of file path checking system so that there cannot be and IOError
######



"""
What I want to happen here is for the program to take the file given in the path variable and do the candidate object operation on each of the
files in the folder until it terminates. 

"""



CandName = Path

NewCand = cand.Candidate(Path, CandName)

DataOut = NewCand.getFeatures(3,3, True)

print(DataOut)

"""
The above commented code worked for getting candidate.py to read data from the pfd file given in the path string
into an array. Ideally we want the code to go through the whole set of files in a directory where the pfd files are located and create a set of csv files
corresponding to the name of each pfd file. 

"""





