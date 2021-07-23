# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 12:03:50 2021

@author: Ryan Craft


Created with the intention of learning how the Candidate.py program works
by attempting to use it to produce the desired data

"""

import Candidate as cand
import PFDFile as pfd
import PFDFeatureExtractor as extractor
CandName = (r"C:\Users\InFolder\1150234552_100_bins_PSR_0034-0721.pfd")


#TestCand = cand.Candidate(r"C:\Users\InFolder\1150234552_100_bins_PSR_0034-0721.pfd", r"C:\Users\InFolder\1150234552_100_bins_PSR_0034-0721.pfd")

#CandData = TestCand.getFeatures(3,3,True)

#print(CandData)


# IMPORTANT
# The Following lines are able to retrieve the Period and the DM from a PFD file in one array
#

Cand2 = pfd.PFD(True, CandName)

#Prof = Cand2.getprofile()

#Data = Cand2.computeFeatures(3)

CandParam = extractor.PFDFeatureExtractor(Cand2)

Params = CandParam.getCandidateParameters(Cand2)

print(Params)