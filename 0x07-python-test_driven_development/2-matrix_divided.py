#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ Divides all elements of a matrix

        Raise:
            TypeError if matrix is not a list of ints or floats.
            TypeError if each row is not the same size
            TypeError div must be a number(int or float)
            ZeroDivisionError if div equals to zero
    """

    n_max = []

    for leng in range(len(matrix)):
        if type(matrix[leng]) != list:
            raise TypeError("matrix must be a\
                     matrix (list of lists) of integers/floats")
        for trav in range(len(matrix[leng])):
            if type(matrix[leng][trav]) != int and\
                    type(matrix[leng][trav]) != float:
                raise TypeError("matrix must be a\
                         matrix (list of lists) of integers/floats")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    long_mat_ze = len(matrix[0])
    for long_lis in range(len(matrix)):
        if len(matrix[long_lis]) != long_mat_ze:
            raise TypeError("Each row of the matrix must have the same size")

    for len_n_max in matrix:
        n_max.append(list(map(lambda ope: round(ope / div, 2), len_n_max)))
    return n_max
