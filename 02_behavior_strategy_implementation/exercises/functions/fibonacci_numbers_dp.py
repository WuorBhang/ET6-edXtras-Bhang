#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# source: https://github.com/nocotan/algorithm_collection/blob/main/algorithm_collection/mathematics/fibonacci_numbers_dp.py

# --- declare function ---

def fibonacci_numbers_dp(n: int) -> int:
    '''
    Calculate the n-th Fibonacci number using dynamic programming. (from bottom to top)
    
    args:
    :type n: int The position of the Fibonacci number to calculate(be >= 0)
    
    return:
    :type: int The n-th Fibonacci number
    
    Maths:
        Fibonacci numbers are defined by F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
        
    Example:
    
    >>> fibonacci_numbers_dp(0) 0  
    >>> fibonacci_numbers_dp(1) 1
    >>> fibonacci_numbers_dp(2) 1
    >>> fibonacci_numbers_dp(3) 2
    >>> fibonacci_numbers_dp(4) 3
    '''
    # initialize the list to store the Fibonacci numbers
    f = [0, 1]
    
    # calculate the Fibonacci numbers from the bottom to the top
    for i in range(2, n+1):
        
        # follow the fibonacci recurrence relation by appending the sum of the last two numbers
        f.append(f[i-1] + f[i-2])
        
    # return the n-th Fibonacci number
    return f[n]

# example
# print(fibonacci_numbers_dp(10)) # 55
# print(fibonacci_numbers_dp(20)) # 6765


# --- test function ---
assert fibonacci_numbers_dp(0) == 0
assert fibonacci_numbers_dp(1) == 1
assert fibonacci_numbers_dp(2) == 1
assert fibonacci_numbers_dp(10) == 55
assert fibonacci_numbers_dp(20) == 6765
assert fibonacci_numbers_dp(30) == 832040
assert fibonacci_numbers_dp(60) == 1548008755920
