# File:parent_hw2a.py
# Author: Jeffery Parent
# Date: September 23, 2021
# Section: 1006 
# E-mail: Jeffery_parent@maine.edu

# Description:
# asks user for the attendance at four labs and outputs the average.

# Collaboration:
# I didn't discuss this assingment with anyone.

print("Hello, I will calculate the lab attendance average.")
l0att=float(input("What was the attendance at Lab 0?"))
l1att=float(input("What was the attendance at Lab 1?"))
l2att=float(input("What was the attendance at Lab 2?"))
l3att=float(input("What was the attendance at Lab 3?"))

avgatt=int(l0att+l1att+l2att+l3att)//4

if l0att>=24:
    print("The average attendance in the first four labs was,", avgatt,".",  
           "Warning! The first lab meeting looks like it exceeded the room capacity!")
elif l1att>=24:
    print("The average attendance in the first four labs was,", avgatt,".",  
           "Warning! The second lab meeting looks like it exceeded the room capacity!")
elif l2att>=24:
    print("The average attendance in the first four labs was,", avgatt,".",  
           "Warning! The third lab meeting looks like it exceeded the room capacity!")
elif l3att>=24:
    print("The average attendance in the first four labs was,", avgatt,".",  
           "Warning! The fourth lab meeting looks like it exceeded the room capacity!")
else: print("The average attendance in the first four labs was,", avgatt,".")




