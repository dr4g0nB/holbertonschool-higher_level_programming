#!/usr/bin/python3
import json


def from_json_string(my_str):
    """ Return
           Object represented by a JSON
    """
    return json.loads(my_str)
