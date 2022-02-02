# File:parent_hw6b.py
# Author: Jeffery Parent
# Date: October 29, 2021
# Section: 1006 
# E-mail: Jeffery_parent@maine.edu

# Description:
# 

# Collaboration:
# I didn't discuss this assingment with anyone.

import statistics
import random

def round():
    total =0
    random.seed()
    roll=0
    rollnumber=0
    eachroll_list=[]
    while total<20 and roll !=1:
        roll =random.randrange(1,7)
        eachroll_list.append(roll)
        print('Roll: ', roll)
        rollnumber+=1
        if roll == 1:
            total = 0
        else:
            total += roll
    print("Turn total: ", total)
    return total, rollnumber, eachroll_list


def main():
    rounds= int(input('How many rounds do you want to play? '))
    total_list=[]
    totalroll_list=[]
    roll_sequence=[]
    while rounds>0:
        total, rollnumber, eachroll_list = round()
        
        total_list.append(total)
        totalroll_list.append(rollnumber)
        roll_sequence.append(eachroll_list)
        
        rounds-=1
        
    print()
    # print(totalroll_list , roll_sequence)
    print(f'Average score: {sum(total_list)/len(total_list)} ')
    print(f'Average run length: {sum(totalroll_list)/len(totalroll_list)}')
    print(f'Shortest run rolls sequence: {roll_sequence[totalroll_list.index(min(totalroll_list))]}')
    print(f'Longest run rolls sequence: {roll_sequence[totalroll_list.index(max(totalroll_list))]}')
main()

