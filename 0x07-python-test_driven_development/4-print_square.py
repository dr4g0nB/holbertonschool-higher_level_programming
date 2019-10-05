#!/usr/bin/python3
def print_square(size):
    """ Prints a square with the chararcter #

        size - lenght of square
        Raise
            TypeError if size is not an int
            ValueError size is less than 0
            TypeError if size is less than 0 and a float
    """

    if size < 0:
        raise ValueError("size must be >= 0")

    if size < 0 and type(size) == float or type(size) != int:
        raise TypeError("size must be an integer")

    for col in range(size):
        for row in range(size):
            print('#', end="")
        print()
