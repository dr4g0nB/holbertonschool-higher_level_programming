#!/usr/bin/python3
def read_file(filename=""):
    """ Reads a txt file and prints it to stdout """

    with open(filename, encoding='utf-8') as op_r:
        re = op_r.read()
        print('{:s}'.format(re), end="")
