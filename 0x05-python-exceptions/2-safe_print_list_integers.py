#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    leng = 0
    for trav in range(x):
        try:
            print("{:d}".format(my_list[trav]), end="")
            leng += 1
        except (TypeError, ValueError):
            continue
    print()
    return leng
