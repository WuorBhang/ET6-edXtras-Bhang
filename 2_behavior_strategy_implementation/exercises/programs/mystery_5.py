#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Module: Reverse input program
Author: bhang@GenZDevOps
Description: This program takes user input in one list and reverses the list by words in the list 
                once the user is done entering text without modifying the original list.
"""

# --- declare the helper function ---

# This function takes a list and returns a reversed copy of the list containing the same elements
def a(b: list) -> list:
    """Creates a reversed copy of a list"""
    c = [] # store the reversed list
    for d in b: # loop through the original list
        c.insert(0, d) # insert the element at the beginning of the reversed list
    return c # return the reversed list


# --- use the helper function in a program ---

e = []

f = None
while f != "": # keep user input until the user enters nothing
    print("\nSaved e: ", e) # Show the saved list
    f = input(
        "Enter some text to add to the list, or enter nothing to finish: "
    )
    if f != "":
        e.append(f) # add the user input to the list

g = a(e) # get reversed version of the list

print("\nHere are your list in reverse order: ", g) # return user list in reverse order
