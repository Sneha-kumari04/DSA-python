"""
Problem: Write a program to print multiplication table of a number.
Approach: 
1. Take a number as input from the user.
2. Use a loop from 1 to 10 to generate multiples.
3. Multiply the input number with the loop variable.
4. Print the result in table format.
"""
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(  n*i)
  
