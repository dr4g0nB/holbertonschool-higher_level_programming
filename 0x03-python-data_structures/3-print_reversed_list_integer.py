#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    my_list.reverse()

    if my_list is None:
        return(my_list)

    for trav in my_list:
        print('{:d}'.format(trav))
