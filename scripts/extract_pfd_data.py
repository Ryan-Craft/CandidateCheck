#! /usr/bin/env python
"""
##Author: Ryan Craft

Getting Pulsar Feature Lab code to reliably extract and save/process data from raw PFD candidate files.
Allows Dr. McSweenys research group to look at the data more closely.
"""
import os
import glob
import sys
import argparse

from pfd_extractor.extract_wrapper import get_common_pfd_data, write_common_pfd_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    A script designed to organise the SMART candidates and look for clustering in period and DM in adjacent beams
    """)
    parser.add_argument('-p', '--pfd_path', type=str, default=',',
                        help='The path to the pfd files')
    parser.add_argument('-o', '--out_file', type=str, default='pfd_data_file.csv',
                        help='The name of the output file containing the pfd data')
    args=parser.parse_args()

    # Get pfd files
    pfd_files = glob.glob("{}/*pfd".format(args.pfd_path))
    if len(pfd_files) == 0:
        print("No pfd files found in {}. Exiting".format(args.pfd_path))
        sys.exit(0)

    pfd_data = get_common_pfd_data(pfd_files)
    write_common_pfd_data(pfd_data, out_file=args.out_file)






















    
    
    
    












    

