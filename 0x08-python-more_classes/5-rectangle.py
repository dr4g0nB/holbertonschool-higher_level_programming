#!/usr/bin/python3
"""
    module `rectangle`
"""


class Rectangle:
    """  """
    def __init__(self, width=0, height=0):
        """  """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ To retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """ To set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ To retrieve height """
        return self.__height

    @height.setter
    def height(self, value):
        """ To set height
            Raise:
                TypeError - if value is not an int
                ValueError - if value is less than zero.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """ Returns the rectangle perimeter """
        if self.width == 0 & self.height == 0:
            return 0
            return print()
        else:
            return (self.__height + self.__width) * 2

    def area(self):
        """ Returns the rectangle area """
        return self.__width * self.__height

    def __str__(self):
        """ Prints the rectangle """
        if self.width == 0 or self.height == 0:
            return ''

        str_rect = ''
        for i in range(self.__height):
            if i == self.height - 1:
                str_rect += str(self.__width * '#')
            else:
                str_rect += str(self.__width * '#') + '\n'
        return str_rect

    def __repr__(self):
        """ Returns a string """
        return 'Rectangle({}, {})'.\
            format(eval(str(self.__width)), eval(str(self.__height)))

    def __del__(self):
        """ Prints a message when it deletes an instance of Rectangle"""
        print('Bye rectangle...')
