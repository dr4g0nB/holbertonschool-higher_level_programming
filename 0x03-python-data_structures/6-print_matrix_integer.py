#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    if len(matrix[0]) == 0:
        print()

    for row in matrix:
        if len(row) > 0:
            for column in range(len(row)):
                if column == len(row) - 1:
                    print('{:d}'.format(row[column]))
                else:
                    print('{:d}'.format(row[column]), end=" ")
