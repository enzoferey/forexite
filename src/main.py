#!/usr/bin/env python
# coding: utf-8

"""
    Get historical data from Forexite.

    -referenced program
    http://kasege.net/forex/archives/2006/09/forexitedl_autoforexite.html
"""

import os
import sys

from download import download

# *** config ***
_STOCK = sys.argv[1]
_START_MONTH = int(sys.argv[2])
_START_YEAR = int(sys.argv[3])
_END_MONTH = int(sys.argv[4])
_END_YEAR = int(sys.argv[5])

print("Starting download for {:d}/{:d}-{:d}/{:d}".format(_START_MONTH,
                                                         _START_YEAR, _END_MONTH, _END_YEAR))


# Output path calculation
output_filename = str(_START_YEAR) + str(_START_MONTH).zfill(2) + \
    '_' + str(_END_YEAR) + str(_END_MONTH).zfill(2) + '.csv'
output_path = '../output/' + output_filename

print("Output will be writen to: {}".format(output_path))

# Check file doesn't exist
if os.path.isfile(output_path):
    print('Output file exist. Please try again after delete.')
    sys.exit()

# Download and format the files
download(_STOCK, _START_YEAR, _START_MONTH, _END_YEAR, _END_MONTH, output_path)

print('Done !!!')
