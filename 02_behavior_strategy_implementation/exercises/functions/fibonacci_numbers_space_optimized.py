#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# source: https://github.com/nocotan/algorithm_collection/blob/main/algorithm_collection/mathematics/fibonacci_numbers_space_optimized.py


# --- declare function ---

def fibonacci_numbers_space_optimized(n):
    '''
    Calculate the n-th Fibonacci number. using space optimized method.
    This keep s tracking of only the last two numbers.
    
    Para:
        n: int - the index of Fibonacci number sequence to calculate.
        
    Return:
        int - the n-th Fibonacci number.
    
    Example:
    >>>>>fibonacci_numbers_space_optimized(0) -> 0
    >>>>>fibonacci_numbers_space_optimized(1) -> 1
    >>>>>fibonacci_numbers_space_optimized(5) -> 5
    >>>>>fibonacci_numbers_space_optimized(10) -> 55
    >>>>>fibonacci_numbers_space_optimized(20) -> 6765
    '''
    
    # First 2 Fibonacci numbers
    a = 0
    b = 1
    
    # To prevent users to Input a negative number
    assert n >= 0

    # This is to Return the n-th Fibonacci depending on the input number value
    if n == 0:
        return 0
    elif n == 1:
        return b
    
    else:
        # Loop through the range of n to calculate the n-th Fibonacci number
        for i in range(1, n):
            
            c = a + b # finding next number in the sequence
            
            a = b # go back to the previous number
            
            b = c # go to the next number/ new number
            
        # Return the n-th Fibonacci number
        return b
    
# Example:
# print(fibonacci_numbers_space_optimized(0)) # 0
# print(fibonacci_numbers_space_optimized(1)) # 1
# print(fibonacci_numbers_space_optimized(5)) # 5
# print(fibonacci_numbers_space_optimized(10)) # 55
# print(fibonacci_numbers_space_optimized(20)) # 6765

# --- test function ---
assert fibonacci_numbers_space_optimized(0) == 0
assert fibonacci_numbers_space_optimized(1) == 1
assert fibonacci_numbers_space_optimized(5) == 5
assert fibonacci_numbers_space_optimized(10) == 55
assert fibonacci_numbers_space_optimized(20) == 6765
assert fibonacci_numbers_space_optimized(30) == 832040
assert fibonacci_numbers_space_optimized(60) == 1548008755920
