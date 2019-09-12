#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv)
    add = 0

    for i in range(argc):
        if i == 0:
            continue
        add = add + int(sys.argv[i])
    print('{:d}'.format(add))
