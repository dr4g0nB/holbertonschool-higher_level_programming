#!/usr/bin/python3
from models.base import Base
""" imported the class Base to create a rectangle """


class Rectangle(Base):
    """ Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x  must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """ Area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints the rectangle to stdout in x & y """
        for eje_y in range(self.__y):
            print()
        for col in range(self.__height):
            print(self.__x * " ", end="")
            for row in range(self.__width):
                print('#', end="")
            print()

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        for k_key, v_value in kwargs.items():
            if k_key == "id":
                self.id = v_value
            if k_key == "width":
                self.__width = v_value
            if k_key == "height":
                self.__height = v_value
            if k_key == "x":
                self.__x = v_value
            if k_key == "y":
                self.__y = v_value

        for possi, trav_args in enumerate(args):
            if possi == 0:
                self.id = trav_args
            if possi == 1:
                self.__width = trav_args
            if possi == 2:
                self.__height = trav_args
            if possi == 3:
                self.__x = trav_args
            if possi == 4:
                self.__y = trav_args

    def __str__(self):
        """ dunder method """
        return ('[Rectangle] ({}) {}/{}- {}/{}'.format(self.id,
                self.__x, self.__y, self.__width, self.__height))
