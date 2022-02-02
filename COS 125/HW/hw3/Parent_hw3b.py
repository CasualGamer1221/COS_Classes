# File:parent_hw3b.py
# Author: Jeffery Parent
# Date: October 8, 2021
# Section: 1006 
# E-mail: Jeffery_parent@maine.edu

# Description:
# Asks the user to enter a number to count to and when conditions are met, prints a message instead of a number.

# Collaboration:
# I didn't discuss this assingment with anyone.


def main():
    number = int(input("How high should I count? "))
    number += 1
    
    for i in range(0, number, 1):
        counter=0
        if i == 0:
            print(i)
        if (i != 0) and (counter==0):
            if (i % 2) == 0:
                if ((i % 5) == 0) and ((i % 9) != 0) and (counter==0):
                    print("Decade!")
                    counter =1
                if ((i % 9) == 0) and (counter==0):
                    print("Dressed to the nines.")
                    counter =1
                elif (counter==0):
                    print("Too many bugs!")
                    counter =1
            if ((i % 5) == 0) and (counter==0) :
                print("Five basketball players on the court at a time.")
                counter =1
            if ((i % 9) == 0) and (counter==0):
                print("The Orono Farmer’s Market starts at 9am on Saturday.")
                counter =1
            if ((i % 125) == 0) and (counter==0) :
                print("COS 125 is the best course ever!")
                counter =1
            elif (counter==0):
                print(i)
            
main()
