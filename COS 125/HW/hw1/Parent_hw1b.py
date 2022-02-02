# File:hw1b.py
# Author: Jeffery Parent
# Date: September 9, 2021
# Section: 1006 
# E-mail: Jeffery_parent@maine.edu

# Description:
# Ask for the price of icecream bar, then calculates cost for 3 w/ sales tax, then outputs total cost after printing a statement.

# Collaboration:
# I didn't discuss this assingment with anyone.



price=input("How much is this ice cream bar?")
price=int(price)

total_cost=3*price*1.055
print("I would like 3 bars. Here is $",total_cost,".")

print("Thank you.")