#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

# Function to check if input is a valid sentence
def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False
    if not text[0].isupper():
        return False
    if not re.search(r'[.!?]$', text):
        return False
    if not re.search(r'\w+', text):
        return False
    return True

# Prompt until valid sentence
sentence = input("Enter a sentence: ")
while not is_sentence(sentence):
    print("This does not meet the criteria for a sentence.")
    sentence = input("Enter a sentence: ")

# Split into words (remove punctuation, lowercase everything)
words_list = re.findall(r'\b\w+\b', sentence.lower())

# Create empty lists
words = []
freqs = []


for w in words_list:
    if w in words:
        idx = words.index(w)
        freqs[idx] += 1
    else:
        words.append(w)
        freqs.append(1)

# Print results
for i in range(len(words)):
    print(f"{words[i]}: {freqs[i]}")

