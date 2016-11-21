#!/usr/bin/python3

# config
import configparser, os

config = configparser.ConfigParser()
config.read(os.path.expanduser('~/.justrc'))

default_config = {
    "github": {
        "username": "pawelabrams"
    },
    "transmission": {
        "credentials": "transmission:transmission"
    }
}

# populate the config with the defaults
for section in default_config.keys():
    if not config.has_section(section):
        config.add_section(section)
    for option, value in default_config[section].items():
        if not config.has_option(section, option):
            config.set(section, option, value)

with open(os.path.expanduser('~/.justrc'), 'w') as f:
    config.write(f)

# imports
import sys
from commands import *

# vars
command = sys.argv[1]
args = sys.argv[2:]

# just do it already
if command in cmds:
    cmds[command](args)