#!/usr/bin/python3
class Square:
    """Defines a square class that will look for int in size
    """
    __size = "size"

    def __init__(self, size=0):
        """Checks if size is int or greater than zero
            Raises:
                TypeError: if size is not an integer
                ValueError: if size is less than zero
        """
        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns area of size by size
        """
        return self.__size * self.__size
