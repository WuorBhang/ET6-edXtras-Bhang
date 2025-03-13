#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Module: Frog input(Case insensitive)
Author: bhang@GenZDevOps
Description: This program takes user input and checks if it is a frog
"""

# empty string to store user input
a = ""

# loop user input in capital/small letters is "frog"
while a.lower() != "frog":
    # showing the correct name if the user input is not frog
    a = input("Please enter a frog: ")

    # checking if the user input are empty
    if a == "":
        print("You entered nothing, try again.")
        
    # checking case insensitive input showing the correct name if the user input is not frog
    elif a.lower() != "frog":
        print('"' + a + '" is not  a frog, try again.') # repeat if the input is not frog

# print the message if the user input is frog
print("thank you for the frog")
