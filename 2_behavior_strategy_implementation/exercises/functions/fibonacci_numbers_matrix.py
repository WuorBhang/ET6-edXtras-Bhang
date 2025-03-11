#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# source: https://github.com/nocotan/algorithm_collection/blob/main/algorithm_collection/mathematics/fibonacci_numbers_matrix.py

# --- declare helper functions ---


def multiply(F: list[list[int]], M: list[list[int]]) -> None:
    '''
    Multiply two matrices F and M of size 2x2, and put the multiplication result back to F.

    This Function implements the matrix multiplication, which is used in calculating the power of a matrix.
    [ F[0][0], F[0][1] ] * [ M[0][0], M[0][1] ]
    [ F[1][0], F[1][1] ] * [ M[1][0], M[1][1] ]


    args:
        F: (list) A 2x2 matrix.
        M: (list) A 2x2 matrix.

    returns:
        None (modifies the F matrix in place).

    examples:
        F = [[1, 1], [1, 0]]
        M = [[1, 1], [1, 0]]

        ->>>> multiply(F, M) -> F = [[2, 1], [1

    '''

    # Multiply the two matrices and store the result in F[][]
    # store the result in temporary variables
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    # overwrite the F  values with the new values
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w



def power(F: list[list[int]], n: int) -> None:
    '''
    Raise fibonacci matrix F to the power n using divide and conquer algorithm.(n-1)
    Transform the matrix F
        F = [[1, 1],
             [1, 0]]

    to the power n-1.
        F^(n-1) = [[F(n), F(n-1)],
                   [F(n-1), F(n-2)]]

    args:
        F: (list) A 2x2 matrix.
        n: (int) The power to raise the matrix to.

    returns:
        None (modifies the F matrix in place).

    examples:
        F = [[1, 1], [1, 0]]
        power(F, 2) -> F = [[2, 1], [1, 1]]

    '''

    # Base case matrix F to the power of 0 or 1
    M = [[1, 1], [1, 0]]

    # Multiply F to the power of n-1, to run the loop n-1 times
    for i in range(2, n + 1):
        multiply(F, M)

# --- declare primary function ---

def fib(n: int) -> int:
    '''
    Calculate the n-th Fibonacci number using matrix exponentiation.

    Fibonacci sequence:
        F(n) = F(n-1) + F(n-2), with base case
        F(0) = 0, F(1) = 1.

    The matrix representation of the Fibonacci sequence:
        [ F(n) ] = [ 1 1 ]^(n-1) * [ F(1) ]
        [ F(n-1) ]   [ 1 0 ]         [ F(0) ]

    args:
        n: (int) The position of the Fibonacci number to calculate(n >= 0).

    returns:
        (int) The n-th Fibonacci number.

    examples:
        ->>>> fib(0) -> 0
        ->>>> fib(1) -> 1
        ->>>> fib(2) -> 1
    '''

    # Represents the Fibonacci matrix transformation
    F = [[1, 1], [1, 0]]

    # F(0) is defined as 0, so return 0 directly to avoid unnecessary calculations
    if (n == 0):
        return 0
    
    # Raise F matrix to the power of n-1
    power(F, n - 1)

    # Store nth Fibonacci number
    return F[0][0]

# example
# print(fib(10))  # 55
# print(fib(24))  # 46368

# --- test function ---

assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(10) == 55
assert fib(24) == 46368
assert fib(30) == 832040
assert fib(60) == 1548008755920
