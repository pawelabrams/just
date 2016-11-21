from subprocess import check_output, STDOUT
from shutil import which


def install_debian(args):
    out = check_output(["sudo", "apt-get", "install", "-y"] + args)
    changed_packages = []
    for line in out.decode("utf-8").splitlines():
        if line[0:2] == '  ':
            changed_packages.append(line[2:])
        if line.find('autoremove') > -1:
            changed_packages = changed_packages[:-1]
    if changed_packages:
        print('Zmieniłem pakiet(y) ' + ' '.join(changed_packages))
    else:
        print('Nie znalazłem pakietu do zmiany')


def install_arch(args):
    out = check_output(["sudo", "pacman", "--noconfirm", "-S"] + args)
    print("Zainstalowane.")


def install(args):
    if which("apt") is not None:
        install_debian(args)
    elif which("pacman") is not None:
        install_arch(args)
