"""

##Date: 18/9/21

##Author: Ryan Craft

##Use:

 Getting Pulsar Feature Lab code to reliably extract and save/process data from raw PFD candidate files.
 Allows Dr. McSweenys research group to look at the data more closely.


##Notes:






"""

# imports

from PFDFile import PFD
import Utilities as Util
import matplotlib.pyplot as plt
import os
import time
import glob
import csv
from mpl_toolkits import mplot3d



# Global Variables
OutFile = ""
Path = ""
CandidatePathList = []
CandidateNameList = []
CandidatePFDList = []
CandidateDataList = []
DMList = []
PeriodList = []
RAList = []
DECList = []


# Taking the user input as PFD file location (Directory containing the PFD's)

Bool1 = False

while Bool1 == False:

    Path = str(input("Enter the full file path of the file containg the PFD's or 'exit' to exit: \n"))
    PathObj = Util.Utilities(Path)
    Bool1 = PathObj.dirExists(Path)
    
    
    if Path.upper() == 'EXIT':
        print("\n ### Program Exit By User ### \n" )
        os._exit(0)

    elif Bool1 == False and Path.upper() != 'EXIT':
        print("\n ## The Path was not found ## \n")

    else:
        print("\n ### Good: Directory Exists ### \n")


# Determining the Output Path by user input or setting one by default

bool2 = False
while bool2 == False:

    OutFile = str(input("\n Insert file PATH for program outputs or press enter to select default:  \n"))

    if OutFile != "":

        OutFileObject = Util.Utilities(OutFile)
        bool2 = OutFileObject.dirExists(OutFile)

        OutPath = OutFile
        
        print("\n ### Good: File exists! ### \n")

        
    elif OutFile == "":
        OutPath = 'Default_OutFile'

        try: 
            os.mkdir(OutPath)
            bool2 = True
            print("\n A default file has been made in the local directory \n")

        except FileExistsError as err:
            print("Error: The Default File is already used, making Default_Out_File_Date&Time")
            OutPath = OutPath + "_" + time.strftime("%Y%m%d-%H%M%S")
            os.mkdir(OutPath)

            pathObj = Util.Utilities(OutPath)
            bool3 = pathObj.dirExists(OutPath)
            
            if bool3 == True:
                bool2 = True

            else:
                print("Failed to make default folder...")
            
    else:
        print("!ERROR!: File name not found!, try again... \n")

# take the PFD's into a list of candidate objects


CandidatePath = Path
for filename in glob.glob(os.path.join(CandidatePath, "*.pfd")):

    CandidatePathList.append(filename)
    #print(CandidatePathList)


# extracting the Data from the PFD's

filename = os.path.join(OutPath, "Data_Set_" + time.strftime("%Y%m%d-%H%M%S") + ".csv")

f = open(filename, 'w')
writer = csv.writer(f)
writer.writerow(["Candidate Name","RA", "DA", "Best DM", "Period (s)"])
index = 0
for i in CandidatePathList:
    
    CandidateDataTemp = []
    CandidateName = os.path.basename(i)
    CandidateNameList.append(CandidateName)

    PFDObject = PFD(False, i)
    CandidatePFDList.append(PFDObject)

    CandidateDataTemp.append(CandidateNameList[index])
    CandidateDataTemp.append(PFDObject.rastr.decode("utf-8")), RAList.append(PFDObject.rastr.decode("utf-8"))
    CandidateDataTemp.append(PFDObject.decstr.decode("utf-8")), DECList.append(PFDObject.decstr.decode("utf-8"))
    CandidateDataTemp.append(PFDObject.bestdm), DMList.append(PFDObject.bestdm)
    CandidateDataTemp.append(PFDObject.topo_p1), PeriodList.append(PFDObject.topo_p1)
    #print(CandidateDataTemp)
       
    writer.writerow(CandidateDataTemp)
    index = index + 1

f.close()


# the DM vs Period Plot
plt.title("DM Vs Period of Candidates")
plt.xlabel("Period (s)")
plt.ylabel("DM")
plt.scatter(PeriodList, DMList)
plt.yscale('Log')
plt.show()

"""
# Period vs RA vs DEC

fig = plt.figure()
ax = plt.axes(projection='3d')

Zline = DMList
Xline = DECList
Yline = RAList

ax.scatter3D(Xline, Yline, Zline)

"""





















    
    
    
    












    

