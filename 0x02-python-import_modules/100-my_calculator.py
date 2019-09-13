#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys

    argc = len(sys.argv)
    
    if argc != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    else:
        if len(sys.argv)[2] == '+':
            print('{:d}'.format(a + b))
        elif len(sys.argv)[2] == '-':
            print('{:d}'.format(a - b))
        elif len(sys.argv)[2] == '*':
            print('{:d}'.format(a * b))
        elif len(sys.argv)[2] == '/':
            print('{:d}'.format(a / b))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
#        print('{:d} '.format(a <operator> <b> = <result>))
