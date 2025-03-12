#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module: List Reversal
Author: bhang@GenZDevOps
Description: This module creates a reversed copy of a list.
"""

# --- declare function ---


def a(b: list) -> list:
    """
    Creates a reversed copy of a list
    
    Reverse the order of the elements in a list starting with new list.
    
    Para:
        b: list - the list to reverse
    
    Return:
        list - a reversed copy of the list
    
    Time Complexity:
        O(n^2  ) due to the insert (0, items) operation repetition
    
    Examples:
    >>>>>a([1, 2, 3, 4, 5]) [5, 4, 3, 2, 1]
    >>>>>a([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>>>>a([1, 3, 5, 7, 9]) [9, 7, 5, 3, 1]
    
    """
    # initialize empty list to store reversed list
    c = []
    
    # change the older to insert elements into the beginning of the new list
    for item in b:
        
        # begin with the last element of the list to create the new list
        c.insert(0, item)
        
        # call for the new list to be print out
    return c

# Examples:
# print(a([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]
# print(a([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(a([1, 3, 5, 7, 9])) # [9, 7, 5, 3, 1]


# --- test function ---
assert a([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
assert a([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
assert a([1, 3, 5, 7, 9]) == [9, 7, 5, 3, 1]
