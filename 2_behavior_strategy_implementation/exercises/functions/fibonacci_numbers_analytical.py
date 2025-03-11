#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# source: https://github.com/nocotan/algorithm_collection/blob/main/algorithm_collection/mathematics/fibonacci_numbers_analytical.py

# --- import things ---

import math

# --- declare function ---

def fibonacci_numbers_analytical(n: int) -> int:
    '''
    Calculate n-th Fibonacci number using analytical solution using Binet's formula.
    
    The Fibonacci numbers are the numbers in the following integer sequence.
        F(n) = F(n-1) + F(n-2), with base case
        F(0) = 0, F(1) = 1.
        
    The formula for the n-th Fibonacci number is given by Binet's formula:
        F(n) = ( (φ^n) / sqrt(5) ), where φ (Pi) is the golden ratio:
        φ = (1 + sqrt(5)) / 2.
        
    args:
        n: (int) The n-th Fibonacci number to calculate (n >= 0).
        
    returns:
        (int) n-th Fibonacci number round to the nearest integer.
        
    examples:
       ->>>> fibonacci_numbers_analytical(0) -> 0
       ->>>> fibonacci_numbers_analytical(1) -> 1
       ->>>> fibonacci_numbers_analytical(2) -> 1
    '''
    
    # The Fibonacci sequence grows based on φ (Pi).
    phi = (1 + math.sqrt(5)) / 2
    
    # Avoids loops and recursion by using Binet's formula.
    fibonacci_number = pow(phi, n) / math.sqrt(5)
    
    # prevents floating point errors by rounding to the nearest integer.
    return round(fibonacci_number)

# --- test function ---
print(fibonacci_numbers_analytical(0) == 0)
print(fibonacci_numbers_analytical(1) == 1)
print(fibonacci_numbers_analytical(2) == 1)
print(fibonacci_numbers_analytical(10) == 55)
print(fibonacci_numbers_analytical(24) == 46368)
