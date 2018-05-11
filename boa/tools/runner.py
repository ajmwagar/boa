import sys
import os
from .util import bcolors, clear, RepresentsInt
from ..attack.mitm import start
from ..attack.wifi import normalMode, monitorMode, startWifi
from ..attack.rat import listen

import atexit

@atexit.register
def restore():
    print(bcolors.OKGREEN + "\nRestoring system settings." + bcolors.ENDC)
    interface = os.popen('ship -i').read()

    # Array of interfaces
    interArr = os.popen('ship -A').read().split(' ')

    if 'Local' in interface:
        interface = interArr[1]

    # Retore wifi
    if 'mon' in interface:
        normalMode(interface)


def run():

    clear()

    # Print loaded modules
    printModule()

    # Take user input as int
    choice = input("\n" + bcolors.BOLD +
                   "Please choose an option\n> " + bcolors.ENDC)

    if (RepresentsInt(choice)):
        # Convert in int
        choice = int(choice)

        # Run list
        if choice == 1:
            clear()
            # print(bcolors.FAIL + "WIP" + bcolors.ENDC)
            startWifi()
            run()
        elif choice == 2:

            clear()
            # run mitm
            start()

            # Recursion
            run()
        elif choice == 3:
            clear()

            # Run RAT Listener
            listen()

            run()

        elif choice == 4:
            clear()
            print(bcolors.OKGREEN + "Goodbye!" + bcolors.ENDC)
            sys.exit(0)
        else:
            clear()
            print(bcolors.FAIL + "Please input a valid option." + bcolors.ENDC)
            run()

    else:
        clear()
        print(bcolors.FAIL + "Please input a valid option." + bcolors.ENDC)

        # Recusive loop
        run()


def printModule():
    print(str(bcolors.HEADER + "Loaded Modules: " + bcolors.ENDC))
    print("1) WiFi Module")
    print("2) MITM Module")
    print("3) RAT Module")
    print("4) Exit boa")


