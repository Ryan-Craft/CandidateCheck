import os
from astropy.time import Time
import csv
import sys
from p_tqdm import p_map
from numpy import array

from pfd_extractor.PFDFile import PFD


def single_pfd_data_read(pfd_file):
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

    PFDObject.computeFeatures(9)
    sn = PFDObject.sn
    
    return candidate_name, period, dm, sn, ra, dec, int(begin.gps), int(end.gps)

def get_common_pfd_data(pfd_files):
    pfd_data = p_map(single_pfd_data_read, pfd_files)
    return pfd_data

def write_common_pfd_data(pfd_data, out_file='pfd_data_file.csv'):
    with open('out_file.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(["#Candidate Name", "Period (s)", "Best DM", "RA", "DEC", "Begin time GPS", "End time GPS"])
        for row in pfd_data:
            spamwriter.writerow(row)
