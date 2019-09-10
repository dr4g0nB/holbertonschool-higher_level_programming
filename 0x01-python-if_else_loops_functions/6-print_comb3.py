#!/usr/bin/python3
numb = 0
while numb < 8:
    num1 = numb
    while num1 <= 9:
        if numb != num1:
            print('{:d}{:d}'.format(numb, num1), end=", ")
        num1 += 1
    numb += 1
print('{:d}{:d}'.format(numb, num1 - 1), sep="")
