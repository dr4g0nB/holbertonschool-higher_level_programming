#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    a = list(tuple_a) + [0, 0]
    b = list(tuple_b) + [0, 0]
    n_list = []

    for trav in range(2):
        n_list.append(a[trav] + b[trav])
    return(tuple(n_list))
