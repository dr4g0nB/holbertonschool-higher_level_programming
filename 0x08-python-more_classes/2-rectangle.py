#!usr/bin/python3
class Rectangle:
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
        """ To set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def perimeter(self):
        """ Returns the rectangle perimeter """
        if self.width == 0 & self.height == 0:
            self.perimeter = 0
        else:
            return (self.__height + self.__width) * 2

    def area(self):
        """ Returns the rectangle area """
        return self.__width * self.__height
