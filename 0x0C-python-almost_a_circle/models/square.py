#!/usr/bin/python3
""" Inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ size property """
        return self.width

    @size.setter
    def size(self, value):
        """ size's setter """
        self.width = value
        self.height = value

    def __str__(self):
        """Returns Square dimensions """
        return ('[Square] ({}) {}/{} - {}'.format(self.id, self.x,
                                                  self.y, self.width))

    def update(self, *args, **kwargs):
        """ Assigns attributes """
        """ args """
        for posit, trav_args in enumerate(args):
            if posit == 0:
                self.id = trav_args
            if posit == 1:
                self.size = trav_args
            if posit == 2:
                self.x = trav_args
            if posit == 3:
                self.y = trav_args

        """ kwargs """
        for k_value, v_value in kwargs.items():
            if k_value == "id":
                self.id = v_value
            if k_value == "size":
                self.size = v_value
            if k_value == "x":
                self.x = v_value
            if k_value == "y":
                self.y = v_value

    def to_dictionary(self):
        """ Returns a dictionary representation of Square """
        sq_dict = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return sq_dict
