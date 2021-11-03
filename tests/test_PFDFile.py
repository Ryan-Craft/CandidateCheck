from PFDFile import PFD

cand = r"C:\Users\Ryan Craft\Desktop\New Feature Extractor\CandPFD\1117643248_100_bins_PSR_1709-1640.pfd"

print("Loading PFD File")


cand_obj = PFD(False, cand)

print("Successful Load")

print('Best DM: ', cand_obj.bestdm)
