# File:parent_hw4c.py
# Author: Jeffery Parent
# Date: October 15, 2021
# Section: 1006 
# E-mail: Jeffery_parent@maine.edu

# Description:
# Asks the user for their favorite Maine food and creates a song from it.
# Collaboration:
# I didn't discuss this assingment with anyone.

def singVerse(food,verses):
    while verses>0:
        print(f'{verses} bottles of {food} on the wall, {verses} bottles of {food},')
        print(f'Take one down, pass it around, {verses - 1} bottles of {food} on the wall.')
        print()
        verses-=1
    if verses==0:
        print(f'Oh, no. All the {food} is gone!')
def main():
    food=input("What is your favorite maine food? ")
    verses=int(input("How many verses do you want to play? "))
    singVerse(food,verses)
main()
    
    
     