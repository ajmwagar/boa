import sys
import os
from .tools.util import help, bcolors, version
from .tools.runner import run


def main():
    if (os.popen('whoami').read() == 'root\n'):
        # Setup args
        args = sys.argv[1:]

        # Handle Arguments
        for arg in args:
            if (arg == "--help" or arg == "-h"):
                help()
                sys.exit(0)
            elif (arg == "--version" or arg == "-v"):
                version()
                sys.exit(0)
                # print('passed argument :: {}'.format(arg))
        # Run into loop
        try:
            run()
            sys.stdout.write('\b\b\r')  # Current solution
            sys.stdout.flush()
        except KeyboardInterrupt:
            sys.exit(0)
    else:
        print(bcolors.FAIL + "Please run Cobra as root." + bcolors.ENDC)
        sys.exit(0)


if __name__ == '__main__':
    main()
