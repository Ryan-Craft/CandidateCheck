"""
Attempt to modify Dr McSweeny's python program which extracts the necessary details from the 
pfd files.

his code is here: https://github.com/robotopia/CandidateCheck/blob/main/ProjectFiles/Bits%20Needed/get_candidate_details.py


"""

import sys
import PFDFile

dataList = []

filename = r"C:\Users\Ryan Craft\Desktop\PulsarCandCode\CandidateCheck\CandidateCheck\InFolder\1150234552_100_bins_PSR_0034-0721.pfd"

cand = PFDFile.PFD(True, filename)

dataList.append(cand.rastr)
dataList.append(cand.decstr)
dataList.append(cand.bary_p1)
dataList.append(cand.bestdm)

print(dataList)

