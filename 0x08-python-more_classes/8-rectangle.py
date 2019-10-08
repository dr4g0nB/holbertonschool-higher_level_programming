#!usr/bin/python3
class Rectangle:
    """ Creates a Rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """  """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
            self.perimeter = 0
            return print()
        else:
            return (self.__height + self.__width) * 2

    def area(self):
        """ Returns the rectangle area """
        return self.__width * self.__height
#        print('#')
#        print(str('#'))

    def __str__(self):
        """ Prints the rectangle """

        str_rect = ''
        i = 0
        for i in range(self.__height):
            if i == self.height - 1:
                str_rect += str(self.__width * self.print_symbol)
            else:
                str_rect += str(self.__width * self.print_symbol) + '\n'
        return str_rect

    def __repr__(self):
        """ Returns a string """
        return 'Rectangle({}, {})'.\
            format(eval(str(self.__width)), eval(str(self.__height)))

    def __del__(self):
        """ Prints a message when it deletes an instance of Rectangle"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """ Static method 

            Return
                Biggest rectangle based on the area
                rect_1 if both have the same value

            Raise
                TypeError if rect_1 is not an instance
                TypeError if rect_2 is not an  instance
        """

        if rect_1 is not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if rect_2 is not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if Rectangle.rect_1 == Rectangle.rect_2:
            return rect_1
