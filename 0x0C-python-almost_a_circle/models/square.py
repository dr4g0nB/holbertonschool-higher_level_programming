#!/usr/bin/python3
from models.rectangle import Rectangle 
""" Inherits from Rectangle """


class Square(Rectangle):
    """ Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization """
        super().__init__(id)
        super().__init__(x)
        super().__init__(y)
        super().__init__(width)
        super().__init__(height)
        self.__height = size
        self.__width = size

    def __str__(self):
        """ Return
                Square dimensions
        """
        return('[Square] ({}) {}/{} - {}'.format(self.id, self.__x, self.__y, self.size))
