#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Module: Reverse input
Author: bhang@GenZDevOps
Description: This program takes user input and reverses it by characters
"""

# --- declare the helper function ---

# helper function to reverse a string
def a(b: str) -> str:
    """ """
    c = ""
    for d in b:
        c = d + c
    return c


assert a("") == "", "Test 0"
assert a("xyz") == "zyx", "Test 1"
assert a("Malayalam") == "malayalaM", "Test 2"
assert a("1729") == "9271", "Test 3"


# --- use the helper function in a program ---


# empty string to store user input
e = ""

# loop user input in capital/small letters that are beginning reversed
while e == "":
    
    # showing the correct name if the user input is empty
    e = input("\nEnter some something to reverse: ")
    if e == "":
        print("Nope, gotta enter something.  Try again.")

# reverse the user input
f = a(e)

# print the reversed user input
print(e, " -> ", f)
