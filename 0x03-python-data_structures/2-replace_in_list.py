#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

    for trav in my_list:

        if idx is None:
            return(my_list)
        elif idx < 0 or idx >= len(my_list):
            return(my_list)
        my_list[idx] = element
        return(my_list)
