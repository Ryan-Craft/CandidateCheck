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

######
# Declare Variables
#
######
Bool1 = False
Path = ""



######
# User Inputs
#
######



print("\n###################### Pulsar Candidate Check ######################\n")


while Bool1 == False:

    Path = input("Insert file PATH to the folder containing PFD candidates or press ENTER to exit: ")
    Path = str(Path)
    PathObj = Util.Utilities(Path)
    Bool1 = PathObj.dirExists(Path)

    if Path == "": # I am sufficiently aware that this code choice is extremely bad and I should feel bad for making it
        Bool1 = True
    
    if Bool1 == False:
        print("\nSpecified PATH was not found\n")


print("\nSpecified path for input PFD's: \n",Path, "\n")

"""
Now that we have a path variable we can take it and use it as both the name of the candidate and the directory for searching for candidates


"""




