#!/usr/bin/python3
def append_write(filename="", text=""):
    """ Appends a string

        Return
            Number of chars added
    """

    with open(filename, encoding="utf-8", mode="a") as op:
        app = op.write(text)
        return(app)
