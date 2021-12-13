#! /usr/bin/env python
"""
Setup for pfd_extractor
"""
from setuptools import setup
from subprocess import check_output

reqs = ['numpy>=1.13.3',
        'matplotlib>=2.1.0',
        'scipy',
        'p_tqdm',
        ]

setup(name="pfd_extractor",
      version="v1.0",
      description="Reads data from PRESTO PFD files",
      url="https://github.com/Ryan-Craft/CandidateCheck.git",
      #long_description=read('README.md'),
      packages=['pfd_extractor'],
      #package_data={'vcstools':['data/*.csv', 'data/*.db']},
      python_requires='>=3.6',
      install_requires=reqs,
      scripts=['scripts/extract_pfd_data.py'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest']
)