from subprocess import check_output, STDOUT
from __main__ import config

github_username = config.get('github', 'username')

def clone(args):
    if args[0].find('/') < 0:
        args[0] = github_username + '/' + args[0]
    out = check_output(['git', 'clone', 'git@github.com:'+args[0]+'.git'], stderr=STDOUT)
    #TODO: check if really cloned!
    print('Sklonowałem repozytorium '+args[0])