import os
import sys
from .util import bcolors, clear


def listen():
    port = int(input("\n" + bcolors.BOLD +
                     "Please enter the port\n> " + bcolors.ENDC))
    print(bcolors.OKGREEN + "Listening on " + str(port) + bcolors.ENDC)
    print(bcolors.OKBLUE + "(C-c) to exit " + bcolors.ENDC)
    os.system('nc -l -p ' + str(port))
    sys.stdout.write('\b\b\r')  # Current solution
    sys.stdout.flush()
    clear()
