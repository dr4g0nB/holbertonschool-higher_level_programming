#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys

    argc = len(sys.argv)
    
    if argc != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    else:
        if sys.argv[2] == '+':
            add = int(sys.argv[1] + sys.argv[3])
            print('{:d}'.format(add))
        elif sys.argv[2] == '-':
           sub = int(sys.argv[1 - 3])
           print('{:d}'.format(a - b))
        elif sys.argv[2] == '*':
            mul = int(sys.argv[1 * 3])
            print('{:d}'.format(a * b))
        elif sys.argv[2] == '/':
            div = int(sys.argv[1 / 3])
            print('{:d}'.format(a / b))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
#        print('{:d} '.format(a <operator> <b> = <result>))
