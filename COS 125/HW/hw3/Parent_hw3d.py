# File:parent_hw3d.py
# Author: Jeffery Parent
# Date: October 8, 2021
# Section: 1006 
# E-mail: Jeffery_parent@maine.edu

# Description:
#Asks the user for 2 numbers and returns and array of their multiples wit x being the number of rows
# and y being the number of columns

# Collaboration:
# I didn't discuss this assingment with anyone.


def main():
    x=int(input("Enter first number: "))
    y= int(input("Enter second number: "))
    
    while ((x>=1)and(y>=1)):
        for n in range(1,y):

            for i in range(1,x+2):
                print(n*i , end="  ")
            print()
        x=int(input("Enter first number: "))
        y= int(input("Enter second number: "))
    
    if (x or y) <0:
        print("Invalid input")

main()