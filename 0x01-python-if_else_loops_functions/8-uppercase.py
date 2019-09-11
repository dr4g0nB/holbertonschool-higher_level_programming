#!/usr/bin/python3
def uppercase(str):

    for leng in str:
        if ord(leng) > 96 and ord(leng) < 123:
            leng = (chr(ord(leng) - 32))
        print('{}'.format(leng), end="")
    print("")
