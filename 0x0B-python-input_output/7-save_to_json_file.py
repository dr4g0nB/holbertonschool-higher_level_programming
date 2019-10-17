#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """ Writes an obj to a .txt """

    with open(filename, encoding="utf-8", mode="w") as op:
        wr = json.dump(my_obj, op)
