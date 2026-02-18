"""
Problem: Write a program to check whether a number is armstrong or not.
Approach: 
1. An Armstrong number is a number where the sum of each digit raised to the power of total digits equals the original number.
2. First, count the number of digits.
3. Store the original number in a temporary variable named as org_num.
4. Extract each digit using % 10, raise it to the digit count, and add to the sum.
5. Compare the sum with the original number to determine the result.
"""
# count digits in  a number
def count_digits(num):
    count = 0
    org_num = num
    while org_num > 0:
        count += 1
        org_num //= 10
    return count

# Armstrong number define
def is_armstrong(num):
    digits = count_digits(num)
    org_num = num
    sum = 0
    while org_num > 0:
        digit = org_num % 10
        sum += digit ** digits 
        org_num //= 10
    return sum == num

num = int(input("Enter a number: "))

if is_armstrong(num):
    print("Armstrong number")
else:
    print("Not a Armstrong number")
