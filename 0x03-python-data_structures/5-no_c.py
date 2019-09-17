#!/usr/bin/python3
def no_c(my_string):

    n_string = ""
    for trav in my_string:
        if trav is not 'c' and trav is not 'C':
            n_string += trav
    return n_string
