#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This program take user input and reverse it
"""
# This is an empty list (a) to store the reversed input by user input
a = ""

# run through the loop to check if the user input is empty
while a == "":
    a = input("Enter some text to reverse: ") # checking if user input some prompt
    if a == "": # checking if the user input is empty
        print("nope, you have to enter something") # prompt user to enter something

# initialize an empty string (b) to store the reversed input
b = ""

# go through each character in (a) that the user input and reverse it
for c in a:
    
    b = c + b # reverse the input by adding the character to the beginning of the string

# print out the reversed input
print("here is your reversed input: " + b)
