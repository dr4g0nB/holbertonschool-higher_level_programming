#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    if my_list is None:
        return(my_list)

    n_list = []
    for trav in my_list:
        if trav % 2 == 0:
            n_list += [True]
        else:
            n_list += [False]
    return n_list
