"""
1. Initialize first two numbers as 0 and 1.
2. Print them.
3. Use a loop to generate next term as sum of previous two.
4. Update the two variables after each iteration.
5. Continue until n terms are printed. 
"""
n = int(input("Enter how many terms: ")) # n is the number of term not a number!
a = 0
b = 1
if n < 0:
        print("Enter a positive number!")
elif n == 0:
        print(a)
elif n == 1:
        print(b)
else:
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        

