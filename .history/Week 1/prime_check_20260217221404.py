num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number!")
else:
    for i in range(2, num):
        if num % 2 == 0:
        print("Not Prime")
    else:
        print("prime number")

