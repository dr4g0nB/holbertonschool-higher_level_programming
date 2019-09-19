#!/usr/bin/python3
def only_diff_elements(set_1, set_2):

    setun = set(set_1)
    setdeux = set(set_2)

    return setun ^ setdeux
