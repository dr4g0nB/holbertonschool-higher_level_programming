#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
absnumber = abs(number) % 10
if number < 0:
    absnumber *= -1
if absnumber < 6 and absnumber != 0:
    print('Last digit of {:d} is {:d} and is less than 6 and not 0'
          .format(number, absnumber))
elif absnumber > 5 and absnumber != 0:
    print('Last digit of {:d} is {:d} and is greater than 5'
          .format(number, absnumber))
else:
    print('Last digit of {:d} is {:d} and is 0'
          .format(number, absnumber))
