#!/usr/bin/python3
def add_integer(a, b=98):
    """ Add two integers
        a and b must be ints.
        If a or b is a float, then cast them into int.

        Raise:
            TypeError - ("a must be an int") or ("b must be an int")
        Return:
            Addition of a and b.
     """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")

    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    if type(a) == float or type(b) == float:
        return int(a) + int(b)
    else:
        return a + b
