#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# source: https://github.com/nocotan/algorithm_collection/blob/main/algorithm_collection/mathematics/fibonacci_numbers_optimized.py


# --- declare globals ---

# Prevent excessive memory allocation while allowing for large values of n
MAX = 1000

# Prevent redundant calculations
f = [0] * MAX

# --- declare function ---

def fibonacci_numbers_optimized(n: int) -> int:
    """
    Calculate the n-th Fibonacci number using an optimized memoization and doubling algorithm
    
    args:
        n: int - the n-th Fibonacci number to calculate
    
    returns:
        int - the n-th Fibonacci number
        
    Example:
    fibonacci_numbers_optimized(5) -> 5
    fibonacci_numbers_optimized(10) -> 55
    fibonacci_numbers_optimized(20) -> 6765
    
    """
    
    # F(0) case to initialize a list to start with 0
    if n == 0:
        return 0
    
    # Avoid unnecessary recursion calls
    if n == 1 or n == 2:
        f[n] = 1
        return f[n]

    # Check if the value has already been calculated yo avoid repetition
    if f[n]:
        return f[n]

    # determine k based on whether n is even or odd
    if n & 1:
        
        # This is to return n is odd
        k = (n + 1) // 2
        
        # This is to return n is even
    else:
        k = n // 2

    # Calculate the n-th Fibonacci number and change the fib to fibonacci_numbers_optimized to avoid redundancy/error
    if n & 1:
        f[n] = (fibonacci_numbers_optimized(k) * fibonacci_numbers_optimized(k) + fibonacci_numbers_optimized(k-1) * fibonacci_numbers_optimized(k-1))
    else:
        f[n] = (2*fibonacci_numbers_optimized(k-1) + fibonacci_numbers_optimized(k))*fibonacci_numbers_optimized(k)

    # stored value of n-th Fibonacci number to avoid redundant calculations in future.
    return f[n]

# Example

# print(fibonacci_numbers_optimized(5)) # 5
# print(fibonacci_numbers_optimized(10)) # 55
# print(fibonacci_numbers_optimized(20)) # 6765

# --- test function ---
assert fibonacci_numbers_optimized(5) == 5
assert fibonacci_numbers_optimized(10) == 55
assert fibonacci_numbers_optimized(20) == 6765
assert fibonacci_numbers_optimized(30) == 832040
assert fibonacci_numbers_optimized(40) == 102334155
