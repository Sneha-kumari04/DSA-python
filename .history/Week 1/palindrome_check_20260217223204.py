"""
Problem: Write a program to check whether a given number is a palindrome.
Approach: Reverse the number and compare with original value.
"""
num = int(input("Enter a number: "))

rev_num = 0

while num > 0:
    count = num % 10
    rev_num = rev_num*10 + count
    num = num // 10

if num == rev_num:
    print("Number is Palindrome ! ")
else:
    print("Not Palindrome")
