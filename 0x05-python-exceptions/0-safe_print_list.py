#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    try:
        leng = 0
        for trav in range(x):
            print('{}'.format(my_list[trav]), end="")
            leng += 1
    except IndexError:
        pass
    print()
    return leng
