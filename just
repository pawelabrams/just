#!/usr/bin/python3

# imports
import sys
from commands import *

# vars
command = sys.argv[1]
args = sys.argv[2:]

# just do it already
if command in cmds:
    cmds[command](args)