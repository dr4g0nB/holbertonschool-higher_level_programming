#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    n_dictionary = a_dictionary.copy()
    for trav in n_dictionary:
        n_dictionary[trav] = n_dictionary[trav]*2
    return n_dictionary
