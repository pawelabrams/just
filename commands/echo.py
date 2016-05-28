from subprocess import check_output, STDOUT

def echo(args):
    out = check_output(["echo", "-n"] + args)
    print(out.decode("utf-8"))