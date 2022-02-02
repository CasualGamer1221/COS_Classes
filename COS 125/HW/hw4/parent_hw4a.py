# File:parent_hw4a.py
# Author: Jeffery Parent
# Date: October 15, 2021
# Section: 1006 
# E-mail: Jeffery_parent@maine.edu

# Description:
# asks the user for parks and their yearly visitors, then outputs data calculated from that

# Collaboration:
# I helped /shared information with 2 people on this assingment in BD138, Jake and Gabe


from statistics import mean
from statistics import median

#Get park data
def park_data():
    park_list=[]
    park_yearly_tourists_list=[]
    parks = 5
    while parks > 0:
        park_name=input('What is one of your favorite Maine parks? ')
        park_list.append(park_name)
        park_yearly_tourists=input(f'How many thousand people visit {park_name} in a year?')
        park_yearly_tourists_list.append(park_yearly_tourists)
        parks -= 1
    return (park_list , park_yearly_tourists_list)


park_namelist , park_attendlist = park_data()  #Global variables because all functions call for them

def attendMin():
    attendminimum=min(park_attendlist)
    parkmin=park_namelist[park_attendlist.index(attendminimum)]
    print(f'The park with the fewest visitors is {parkmin} with {attendminimum} thousand.')

def attendMax():
    attendmaximum = max(park_attendlist)   
    parkmax=park_namelist[park_attendlist.index(attendmaximum)]
    print(f'The park with the Most visitors is {parkmax} with {attendmaximum} thousand.')
    
def attendTotal():
    parkattend_total = sum([int(x) for x in park_attendlist])
    print(f'The total number of visitors at those parks is {parkattend_total} thousand.')
    
def attendAvg():
    parkattend_avg= mean([int(x) for x in park_attendlist])
    print(f' The average number of visitors per park is {parkattend_avg} thousand.')

def attendMedian():
    parkattend_median=median([int(x) for x in park_attendlist])
    print(f' The median number of visitors per park is {parkattend_median} thousand.')


def main():
   attendMax()
   attendMin()
   attendTotal()
   attendAvg()
   attendMedian()
        
main()