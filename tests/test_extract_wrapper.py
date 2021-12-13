#! /usr/bin/env python3
"""
Tests the extract_wrapper.py script
"""
import os

from pfd_extractor.extract_wrapper import get_common_pfd_data


def test_get_common_pfd_data():
    """
    Tests the get_common_pfd_data function
    """
    pfd_data = get_common_pfd_data(['tests/test_files/1117643248_100_bins_PSR_1709-1640.pfd'])
    expected_data = [['1117643248_100_bins_PSR_1709-1640.pfd', 0.653056339289927, 24.891, '17:09:26.4400', '-16:40:57.7300', 1117643268, 1117645528]]

    # Compare test
    if pfd_data != expected_data:
        raise AssertionError()


if __name__ == "__main__":
    """
    Tests the relevant functions in sn_flux_est.py
    """

    # introspect and run all the functions starting with 'test'
    for f in dir():
        if f.startswith('test'):
            print(f)
            globals()[f]()