#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ Reads n lines of a .txt ans prints it """

    with open(filename, encoding="utf-8") as op_r:
        if nb_lines > 0:
            for i in range(nb_lines):
                pr_l = op_r.readline()
                print(pr_l, end="")
        else:
            print(op_r.read(), end="")
