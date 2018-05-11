import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def help():
    print(bcolors.BOLD + "Welcome to cobra" + bcolors.ENDC)
    print("-v     --version: print version of cobra")
    print("-h     --help: prints this help message")

def version():
    print('1.0b')

clear = lambda: os.system('clear')

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
