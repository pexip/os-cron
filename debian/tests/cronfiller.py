#! /usr/bin/python3
# this program can be used as a special editor. Example:
# EDITOR=$(pwd)/confiller.py crontab -u dummy -e
# this file is a dependency of the test check_significant_header

import sys
import os
import time

# get the data from the crontab
with open(sys.argv[1]) as infile:
    lines = infile.read()
    
# add a new line (or some more, if LINES is defined in the environment)
# to the crontab

otherlines = os.environ.get("LINES")
if otherlines:
    if otherlines[-1] != '\n':
        otherlines += '\n'
    lines += otherlines
else:
    # by default, add at least one line
    lines += "* * * * * /bin/ls\n"

# wait just a short time to ensure that the crontab file will be
# correctly managed.
time.sleep(1)
with open(sys.argv[1], "w") as outfile:
    outfile.write(lines)
