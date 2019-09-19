#!/usr/bin/python3
def search_replace(my_list, search, replace):

    n_list = []
    for trav in my_list:
        if trav == search:
            n_list.append(replace)
        n_list.append()
    return(n_list)
