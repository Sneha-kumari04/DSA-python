"""
Problem: Write a program to check whether a given number is a palindrome.
Approach: By using operators and while loop with if-else conditional statements.
"""
num = int(input("Enter a number: "))

rev_nu = 0
while num > 0:
    count = num % 10
    rev = rev*10 + count
    num = num // 10

if num == rev:
    print("Number is Palindrome ! ")
else:
    print("Not a Palindrome")
