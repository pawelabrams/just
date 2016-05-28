from subprocess import check_output, STDOUT
from __main__ import transmission_credentials

def check_downloads():
    out = check_output(["transmission-remote", "-n", transmission_credentials, "-l"])
    print(out.decode('utf-8'))

def check(args):
    if args[0][:8] == 'download':
        return check_downloads()