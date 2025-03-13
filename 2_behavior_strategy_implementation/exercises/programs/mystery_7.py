#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module: Search for a query within a user-entered phrase.

Author: bhang@GenZDevOps

Description: This script prompts the user to enter a phrase and a search query.
             The user can specify whether the search should be case-sensitive.
             The program then checks if the query exists within the phrase and displays the result.
"""

# --- Get a valid phrase from the user ---

while True:  
    # Continuously prompt the user until they provide a valid phrase.
    phrase = input("Enter a phrase to search: ")  # Request user input for a phrase.

    if phrase:  # Ensures the user does not enter an empty string.
        confirm = input(f"Is this correct? '{phrase}' (yes/no): ").strip().lower()
        # Ask for confirmation to avoid mistakes.

        if confirm == "yes":  # If the user confirms, exit the loop.
            break

# --- Ask the user if they want case-sensitive search ---

case_sensitive = input("Do you want a case-sensitive search? (yes/no): ").strip().lower() == "yes"
# Stores True if the user selects "yes", otherwise stores False.

# --- Get a valid search query from the user ---

while True:  
    # Continuously prompt the user until they provide a valid search query.
    query = input("Enter a search query: ")  # Request input for the search query.

    if query:  # Ensures the query is not empty.
        confirm = input(f"Is this correct? '{query}' (yes/no): ").strip().lower()
        # Ask for confirmation to prevent errors.

        if confirm == "yes":  # If confirmed, exit the loop.
            break

# --- Perform the search operation based on case sensitivity preference ---

if case_sensitive:  
    phrase_includes_query = query in phrase  # Case-sensitive search: exact match is required.
else:
    phrase_includes_query = query.lower() in phrase.lower()  
    # Case-insensitive search: both phrase and query are converted to lowercase.

# --- Display the result ---

does_or_not = "does" if phrase_includes_query else "does not"
# Constructs a readable output message based on search results.

print(f'"{phrase}" {does_or_not} include "{query}"\nCase sensitive: {case_sensitive}')
# Prints whether or not the phrase contains the query, including case sensitivity status.
