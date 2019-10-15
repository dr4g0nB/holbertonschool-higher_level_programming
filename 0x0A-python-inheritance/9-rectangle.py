#!/usr/bin/python3
""" Class BaseGeometry
"""


class BaseGeometry:
    """ Geometry shapes """
    def area(self):
        """ Area

            Raise
            Excetion if area its not implemented.

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Validates for ints

            Raise
            TypeError if value its not an int.
            ValueError if value is less or equal than 0.
        """
        self.name = name
        self.value = value

        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Subclass """
    def __init__(self, width, height):
        """ Initialization """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__height = height
        self.__width = width

    def area(self):
        """ area """
        return self.__width * self.__height

    def __str__(self):
        """ str """
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))
