#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """ Prints My name is <first name> <last name>

        Rise
            TypeError if last_name ot first_name are not string.
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("first_name must be a string")

    print('My name is {:s} {:s}'.format(first_name, last_name))
