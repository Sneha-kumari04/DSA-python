"""
Prroblem: Write a program to count digits in a number and also print the sum of the digits.
Approach: Using  while loop and remainder(%) operator for counting digits.
"""
# count digits in  a number
def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

# sum of the digits 
def sum_digits(num):
    sum = 0
    while num > 0:
        remain = num % 10
        sum += remain
        num //= 10 
    return sum
    
num = int(input("Enter a number:"))

print("total count of digits are = ", count_digits(num))
print("Sum of the digits in a given number = ", sum_digits(num))