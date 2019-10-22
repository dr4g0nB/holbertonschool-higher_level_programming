#!/usr/bin/python3
""" Class Base """
import json
import os


class Base:
    """ Clase Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """self.id = id"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        e_str = " "
        e_list = []

        for trav in list_objs:
            e_list.append(trav.to_dictionary())
            e_str = cls.to_json_string(e_list)

        with open(filename, encoding="utf-8", mode="w") as wr:
            wr.write(e_str)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Square":
            ins = cls(1)

        if cls.__name__ == "Rectangle":
            ins = cls(1, 1)

        ins.update(**dictionary)
        return ins

    """@classmethod
    def load_from_file(cls):"""
        """ Returns a list of instances """
        """filename = cls.__name__ + ".json"
        if os.path.exits(filename):
            return
        else:
            return []"""
