#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        """
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Checks if size is int or greater than zero
                Raises:
                    TypeError: if size is not an integer
                    ValueError: if size is less than zero
        """
        if type(value) != int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        """
        return self.__position
      
    @position.setter
    def position(self, value):
        """
        """ 
        if tuple(value) != int & tuple(calue) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns area of size by size
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints an empty line
        """
        if self.__size == 0:
            print()
        else:
            for col in range(self.__size):
                for row in range(self.__size):
                    print('#', end="")
                print()
