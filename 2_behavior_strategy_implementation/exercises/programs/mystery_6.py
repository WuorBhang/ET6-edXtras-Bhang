#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module: enter a sentence with at least two words.

Author: bhang@GenZDevOps

Description: This script asks the user to enter a sentence with at least two words.
                The user is then prompted to decide whether to keep or remove each word.
                    Finally, the remaining words are displayed as a new sentence.
"""


sentence = ""  # Stores the user's input sentence.


while True:  # Infinite loop to ensure valid input is provided.
    sentence = input("Enter a sentence with at least 2 words: ")  # Ask for user input.

    if sentence is None:  # Checks if input is None (shouldn't normally happen with input()).
        print("There is no escape")  # Displays a message and re-prompts the user.

    elif len(sentence) < 3:  # Ensures the sentence is long enough to contain two words.
        print(f'"{sentence}" is too short to have two words')  # Warns the user.

    elif " " not in sentence:  # Checks if there is at least one space (ensuring two words).
        print("There is no space")  # Informs the user that only one word was entered.

    else:
        break  # If all conditions are met, exit the loop.

# --- Process the sentence ---

words = sentence.split()  # Splits the sentence into a list of words.
new_sentence = []  # Creates an empty list to store the words the user chooses to keep.

# --- Ask the user which words to keep ---

for word in words:  # Loops through each word in the original sentence.
    keep = input(f"Do you want to keep this word? (yes/no): {word}\n").strip().lower()
    # Asks the user if they want to keep the word, ensuring consistent formatting.

    if keep == "yes":  # If the user chooses to keep the word:
        new_sentence.append(word)  # Add the word to the new sentence list.

# --- Display the final sentence ---

print(" ".join(new_sentence))  # Joins and prints the remaining words as a sentence.
