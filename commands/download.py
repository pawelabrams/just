from subprocess import check_output, STDOUT
from __main__ import config

transmission_credentials = config.get('transmission', 'credentials')

def torrent(filename):
    out = check_output(["transmission-remote", "-n", transmission_credentials, "-a", filename])
    if not out:
        print('Wszystko poszło jak po maśle; sprawdź postęp just check downloads')

def download(args):
    if args[0][:14] == 'https://kat.cr':
        import gzip
        from urllib.request import urlopen
        with urlopen(args[0]) as r:
            gzipFile = gzip.GzipFile(fileobj=r)
            re = gzipFile.read().decode('utf-8').splitlines()
            for line in re:
                if line.find('data-download') > -1:
                    torrent('http://'+line.split('//')[1].split('"')[0])
                    break
    elif args[0][-8:] == '.torrent':
        return torrent(args[0])