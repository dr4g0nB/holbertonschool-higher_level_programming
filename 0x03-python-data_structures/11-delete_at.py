#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    if my_list is None:
        return(my_list)

    if idx < 0 or idx > len(my_list):
        return(my_list)
    else:
        del my_list[idx]
#        n_list += tra
    return(my_list)
