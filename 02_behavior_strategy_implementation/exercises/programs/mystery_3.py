#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Module: Cat input(Case insensitive)
Author: bhang@GenZDevOps
Description: This program takes user input and checks if it is a cat
"""

# empty string to store user input
a = ""

# loop user input in capital/small letters is "cat"
while "cat" not in a.lower():
    
    # showing the correct name if the user input is not cat
    a = input('Please enter something containing "cat": ')
    
    # checking if the user input are empty
    if a == "":
        print("You entered nothing, try again.")
        
        # checking case insensitive input showing the correct name if the user input is not cat
    elif "cat" not in a.lower():
        print('"' + a + '" does not contain cat, try again.')

# print the message if the user input is cat
print("thank you for the cat")
