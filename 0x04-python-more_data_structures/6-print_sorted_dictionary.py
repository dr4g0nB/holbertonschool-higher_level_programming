#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    for un in sorted(a_dictionary):
        print('{} : {}'.format(un, a_dictionary[un]))
