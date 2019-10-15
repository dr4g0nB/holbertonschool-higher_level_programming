#!/usr/bin/python3
""" Subclass"""


class MyInt(int):
    """ Subclass from int """
    def __eq__(self, other):
        """ magic function """
        return(int(self) != int(other))

    def __ne__(self, other):
        """ magic function """
        return(int(self) == int(other))
