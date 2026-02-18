"""
Problem: Write a program to print the following pattern- 
              *****
              ****
              ***
              **
              *            
Approach: 
1. Use a loop to control number of rows.
2. Print stars in decreasing number of rows which is 5.
"""
for i in range(6,0,-1):
      print("*" * i)
