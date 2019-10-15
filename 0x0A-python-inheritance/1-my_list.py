#!/usr/bin/python3
""" A class that inherits.
"""


class MyList(list):
    """ Inherits from list """
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        print(sorted(self))
