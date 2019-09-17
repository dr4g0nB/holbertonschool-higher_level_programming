#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    n_list = my_list.copy()

    if my_list is None:
        return(n_list)
    elif idx < 0 or idx > len(my_list):
        return(n_list)
    else:
        for trav in n_list:
            n_list[idx] = element
            return(n_list)
