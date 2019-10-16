#!/usr/bin/python3
def write_file(filename="", text=""):
    """ Writes a string to a .txt

        Return
           Number of chars written
    """

    with open(filename, encoding="utf-8", mode="w") as op:
        wr = op.write(text)
    return(wr)
