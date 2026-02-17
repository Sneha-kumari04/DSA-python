"""
Program: Write a program to reverse a given positive integer.
Approach: By using operators and while loop.
"""
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    count = num % 10
    rev_num = rev * 10 + num

