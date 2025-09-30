#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
term = input("Enter number of terms: ")


for i in range(1):   
    if term.isdigit():
        term = int(term)
        if term > 0:
            a, b = 0, 1
            j = 0   
            for j in range(term):   
                print(a, end=" ")
                a, b = b, a + b
        else:
            print("Please enter a positive integer.")
    else:
        print("Please enter a positive integer.")
