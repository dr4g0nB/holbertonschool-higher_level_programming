#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv)

    if argc == 1:
        print('{:d} arguments.'.format(argc - 1))
    elif argc == 2:
        print('{:d} argument:'.format(argc - 1))
        print('1: {}'.format(sys.argv[1]))
    else:
        print('{:d} arguments:'.format(argc - 1))
        for i in range(argc):
            if i != 0:
                print('{:d}: {}'.format(i, sys.argv[i]))
