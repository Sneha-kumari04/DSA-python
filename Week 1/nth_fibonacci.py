"""
Problem: Write a program to find the nth term in the Fibonacci sequence.
"""
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num -1) + fib(num -2)
    

num = int(input("Enter a number "))
print("Fibonacci number is:", fib(num))