#!/usr/bin/python3
def number_of_lines(filename=""):
    """ Return
            Number of lines of a text file
    """

    with open(filename) as num_l:
        lines = num_l.readlines()
    return len(lines)
