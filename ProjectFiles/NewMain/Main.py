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
import numpy as np
import time


######
# Declare Variables
#
######

localTime = time.asctime( time.localtime(time.time()))

Bool1 = False
Bool2 = False
Path = ""
CandidateList = []
CandidateNameList = []
CandidateDataList = []
DefaultNo = 0

######
##### User Inputs:
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

    Path = str(input("Insert file PATH to the folder containing PFD candidates or enter 'exit' to exit: \n"))
    PathObj = Util.Utilities(Path)
    Bool1 = PathObj.dirExists(Path)

    if Path == "exit": 
        print("\n### Program Exit by User ###\n")
        os._exit(0)
    
    if Bool1 == False and Path !="Exit":
        print("\nSpecified PATH was not found\n")




"""
PSEUDO CODE: Designating the file PATH for the CSV's

Ask the user if they are using an existing folder, want to create a new local folder or default folder for the output folder or exit

If the user selects an existing folder, use loop similar to the input folder loop above to get the correct input from the user and

Elif the user decides to create a new folder:
    prompt the user to input a valid name for the folder
    use python code to create the directory in the local file with name specified by the user

    Use utilities to check that the file path exists otherwise, throw and error and create a default folder

Elif the user decides to use the default file location, create a default folder in the local dir

"""
while Bool2 == False:
    Select = str(input("\n Send Output to: Existsing folder (E), New Local Folder (N) or Default Folder (D)\n"))

    if Select == "E":
        OutPath = str(input("Insert file PATH to the folder containing PFD candidates or enter 'exit' to exit: \n"))
        PathObj1 = Util.Utilities(OutPath)
        Bool2 = PathObj1.dirExists(OutPath)

        if Path == "exit": 
            print("\n### Program Exit by User ###\n")
            os._exit(0)
    
        else:
            print("\nSpecified PATH was not found or 'exit' command was not input correctly\n")


    elif Select == "N":
        try:
            OutPath = str(input("Enter the name of the Folder to be created in the local directory or exit (exit): "))
            
            if OutPath == "exit": 
                print("\n### Program Exit by User ###\n")
                os._exit(0)

            else:
                print()
            
            os.mkdir(OutPath)
            Bool2 = True

        except FileExistsError as err:
            print(err)
            print("\n That file name already exists, please try a different one... \n") 

        print("Folder created successfully!")
        
    elif Select == "D":
        
        try:
            
            OutPath = 'Default_Out_File'
            os.mkdir(OutPath)
            
            Bool2 = True

        except FileExistsError as err:
            print(err)
            OutPath = 'Default_Out_File ' + 'str(localTime)'
            os.mkdir(OutPath)
            #print("\n Default Folder already exists, creating: 'Default_Out_File " + str(localTime), "'")
            Bool2 = True
        
    else:
        print("\n That command is not listed, please try again or exit the program... \n")
        Bool2 = False
            



print("\n### Output PATH Selected: ", OutPath, "\n")




########try:



######
##### File Reading loop: creating arrays for holding the object data (appending them to a list for later) using candidate.py
# --- Loop which navigates to the file path and then creates an object for each file in the folder
# --- loops appends each candidate object to a list.
# --- For each object in the list, the array associated with its parameters is written into a unique csv file
# --- we dont want it to make plots because it will slow everythin down (plots are disabled in PFDfeatureExtractor and FeatureExtractor)
######

"""
What I want to happen here is for the program to take the file given in the path variable and do the candidate object operation on each of the
files in the folder until it terminates. 

"""
#Below code modified from StackOverflow: https://stackoverflow.com/questions/18262293/how-to-open-every-file-in-a-folder

startTime = time.time()

CandidatePath = Path
for filename in glob.glob(os.path.join(CandidatePath, "*.pfd")):
  with open(filename, 'rb') as f:
    CandidateName = os.path.basename(filename)
    CandidateNameList.append(CandidateName)
    NewCand = cand.Candidate(filename, filename)
    CandidateList.append(NewCand)
    CandidateData = NewCand.getFeatures(3,3,True)
    CandidateDataList.append(CandidateData)

print(CandidateNameList)
#print(CandidateDataList)

######
##### File Output: Sends data contanied in the Lists to a CSV file named with the Candidate Name
# --- Loop that creates a csv file with filename equal to the basename of the pulsar pfd file 
# --- Use numpy savetxt function to write the data to the csv file
# --- Continue for all csv files in the list
# --- 
######


# The below code uses os path functions found on note.nkmk.me: https://note.nkmk.me/en/python-os-basename-dirname-split-splitext/
# and from Delft Stack: https://www.delftstack.com/howto/python/python-write-array-to-csv/#:~:text=We%20can%20write%20an%20array%20to%20a%20CSV%20file%20by,to_csv()%20method.
index = 0
cwd = os.getcwd()
out = os.chdir(OutPath)
for i in CandidateList:
    BaseNameNoExt = os.path.splitext(os.path.basename(CandidateNameList[index]))[0]
    np.savetxt(str(BaseNameNoExt) + ".csv", CandidateDataList[index], delimiter=",") #Needs to have user input
    index = index + 1
os.chdir(cwd)

endTime = time.time()
elapsedTime = (endTime - startTime)
print(elapsedTime)