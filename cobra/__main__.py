import sys
from .util import help, bcolors, clear, version
from .runner import run

done = False


def main():
    args = sys.argv[1:]

    for arg in args:
        if (arg == "--help" or arg == "-h"):
            help()
            sys.exit(0)
        elif (arg == "--version" or arg == "-v"):
            version()
            sys.exit(0)
            # print('passed argument :: {}'.format(arg))
    run()


if __name__ == '__main__':
    main()
