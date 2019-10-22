#!/usr/bin/python3
""" Class Base """
import json


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

        with open(filename, encoding="utf-8", mode="w") as wr:
            e_list = []
            if list_objs is None:
                wr.write(cls.json_string([]))
            else:
                for content in list_objs:
                    e_list.append(content.to_dictionary())
                json_list = cls.to_json_string(e_list)
                wr.write(json_list)

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
            ins = cls(1, 0, 0)

        if cls.__name__ == "Rectangle":
            ins = cls(1, 1, 0, 0)

        ins.update(**dictionary)
        return ins

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        json_file = cls.__name__ + ".json"

        try:
            with open(json_file) as op:
                inside = op.read()
                json_data = cls.from_json_string(inside)

                e_list = []

                return [cls.create(**data) for data in json_data]
        except FileNotFoundError:
            return []
