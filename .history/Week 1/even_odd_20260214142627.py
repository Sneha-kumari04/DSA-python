"""
Problem: Check whether the number is even or odd.
Approach: Using if-elif-else loop for checking the number.
"""
n = int(input("Enter a number:"))

if n > 0:
    if n % 2 == 0:
        print("Even number")
    elif n % 2 != 0:
        print("Odd number")
