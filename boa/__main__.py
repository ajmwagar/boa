import sys
import os
from time import sleep
from .tools.util import help, bcolors, version, clear
from .tools.process import Process
from .tools.runner import run


def dependency_check():
    ''' Check that required programs are installed '''
    required_apps = ['airmon-ng', 'iwconfig', 'ifconfig', 'aircrack-ng',
                     'aireplay-ng', 'airodump-ng', 'ship', 'netcat', 'nc', 'mdk3', 'mitmf']
    optional_apps = []
    missing_required = False
    missing_optional = False

    for app in required_apps:
        if not Process.exists(app):
            missing_required = True
            print(
                bcolors.FAIL + '{!} {R}error: required app {O}%s{R} was not found' % app + bcolors.ENDC)

    for app in optional_apps:
        if not Process.exists(app):
            missing_optional = True
            print(bcolors.WARNING +
                  '{!} {R}error: recomended app {O}%s{R} was not found' % app + bcolors.ENDC)

    if missing_required:
        print(bcolors.FAIL +
              '{!} {R}required app(s) were not found, exiting.{W}' + bcolors.ENDC)
        sys.exit(-1)

    if missing_optional:
        print(bcolors.FAIL +
              '{!} {O}recommended app(s) were not found' + bcolors.ENDC)
        print(bcolors.FAIL +
              '{!} {O}boa may not work as expected{W}' + bcolors.ENDC)


def main():
    if (os.popen('whoami').read() == 'root\n'):
        # Setup args
        args = sys.argv[1:]

        # Handle Arguments
        for arg in args:
            if (arg == "--help" or arg == "-h"):
                clear()
                intro()
                help()
                sys.exit(0)
            elif (arg == "--version" or arg == "-v"):
                version()
                sys.exit(0)
                # print('passed argument :: {}'.format(arg))

        # Run into loop
        dependency_check()
        try:
            clear()
            intro()
            sleep(3)
            run()
            sys.stdout.write('\b\b\r')  # Current solution
            sys.stdout.flush()
        except KeyboardInterrupt:
            sys.exit(0)
    else:
        print(bcolors.FAIL + "Please run Boa as root." + bcolors.ENDC)
        sys.exit(0)


def intro():
    print(bcolors.OKGREEN + '888\n888\n888\n88888b.  .d88b.  8888b.\n888 "88bd88""88b    "88b\n888  888888  888.d888888\n888 d88PY88..88P888  888\n88888P"  "Y88P" "Y888888\n                     ' + bcolors.ENDC)
    print(bcolors.WARNING + "\n         ,,'6\'\'-,.\n        <====,.;;--.\n        _`---===. \"\"\"==__\n      //\"\"@@-\===\@@@@ \"\"\\\\\n     |( @@@  |===|  @@@  ||\n      \\ @@   |===|  @@  //\n        \\ @@ |===|@@@ //\n         \\  |===|  //\n___________\\|===| //_____,----\"\"\"\"\"\"\"\"\"\"-----,_\n  \"\"\"\"---,__`\===`/ _________,---------,____    `,\n             |==||                           `\   \n            |==| |                             )   |\n           |==| |       _____         ______,--\'   \'\n           |=|  `----\"\\""     `\"\"\"\"\"\"\"\"'_,-'\n            `=\     __,---\"\"\"-------------\"\"\"\'\'\n                \"\"\"\"\n")
    print('\n' + bcolors.OKGREEN + 'Developed by ajmwagar' + bcolors.ENDC)


if __name__ == '__main__':
    main()
