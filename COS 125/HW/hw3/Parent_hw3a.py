# File:parent_hw3a.py
# Author: Jeffery Parent
# Date: October 8, 2021
# Section: 1006 
# E-mail: Jeffery_parent@maine.edu

# Description:
# Asks the user for numbers until stop is inputted. 
# Then prints the largest number entered.

# Collaboration:
# I didn't discuss this assingment with anyone.



def main():
    largest= None

    while True:
        number=input("Enter a number (or 'stop' to end): ")
        if number == "stop":
            break 
        number=int(number)
        
        if largest == None:
            largest=number
        elif largest < number:
            largest=number
            
    print ("The largest number is: ",largest)
main()