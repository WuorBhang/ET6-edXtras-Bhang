#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# source: https://github.com/nocotan/algorithm_collection/blob/main/algorithm_collection/mathematics/fibonacci_numbers.py

# --- declare function ---

def fibonacci_numbers(n: int) -> int:
    '''
    Recursively calculate the n-th Fibonacci number.
        this follow the definition of Fibonacci numbers:
        F(n) = F(n-1) + F(n-2)
        
    Para:
        n: int - the n-th Fibonacci number to calculate
        
    Return:
        int - the n-th Fibonacci number
    
    # Examples:
    >>>>>fibonacci_numbers(0) -> 0
    >>>>>fibonacci_numbers(1) -> 1
    >>>>>fibonacci_numbers(5) -> 5
    >>>>>fibonacci_numbers(10) -> 55
    >>>>>fibonacci_numbers(20) -> 6765
    >>>>>fibonacci_numbers(60) -> 1548008755920
    '''
    
    # checking for the input value of n, if n is a non-negative integer
    assert n >= 0

    # base case to return 0 or 1 the value of n if it is 0 or 1
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        # recursively calculating the n-th Fibonacci number using F(n) = F(n-1) + F(n-2) to return the final value
        return fibonacci_numbers(n-1) + fibonacci_numbers(n-2)


# Examples:
# print(fibonacci_numbers(0)) # 0
# print(fibonacci_numbers(1)) # 1
# print(fibonacci_numbers(5)) # 5
# print(fibonacci_numbers(10)) # 55
# print(fibonacci_numbers(20)) # 6765
# print(fibonacci_numbers(60)) # 1548008755920

# --- test function ---

assert fibonacci_numbers(0) == 0
assert fibonacci_numbers(1) == 1
assert fibonacci_numbers(5) == 5
assert fibonacci_numbers(10) == 55
assert fibonacci_numbers(20) == 6765
assert fibonacci_numbers(60) == 1548008755920
