#!/usr/bin/python3
""" Class Base """


class Base:
    """ private class attribute - __nb_objects = 0
        class constructor - def __init__(self, id=None):
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """self.id = id"""

        if id is not None:
            self.id = id
        else:
            """self.id = self.__nb_object"""
            #self.id = id

            Base.__nb_objects += 1
            self.id = Base.__nb_objects
