import os
from astropy.time import Time
import csv

from pfd_extractor.PFDFile import PFD


def get_common_pfd_data(pfd_files):
    pfd_data = []
    for pfd_file in pfd_files:
        candidate_name = os.path.basename(pfd_file)

        # Read in pfd with PFD class
        PFDObject = PFD(False, pfd_file)

        # Get data we require
        ra  = PFDObject.rastr.decode("utf-8")
        dec = PFDObject.decstr.decode("utf-8")
        period = PFDObject.topo_p1
        #period = PFDObject.bary_p1
        dm = PFDObject.bestdm

        # Work out start and end time in GPS
        times = PFDObject.start_topo_MJDs
        begin, end = Time([times[0], times[-1]], format='mjd') 
        
        pfd_data.append([candidate_name, period, dm, ra, dec, int(begin.gps), int(end.gps)])
    return pfd_data

def write_common_pfd_data(pfd_data, out_file='pfd_data_file.csv'):
    with open('out_file.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(["#Candidate Name", "Period (s)", "Best DM", "RA", "DEC", "Begin time GPS", "End time GPS"])
        for row in pfd_data:
            spamwriter.writerow(row)
