# File:parent_hw4b.py
# Author: Jeffery Parent
# Date: October 15, 2021
# Section: 1006 
# E-mail: Jeffery_parent@maine.edu

# Description:
# Asks the user for park name, visitors, and favorite feature, then celebrates a feature chosen by the user.

# Collaboration:
# I didn't discuss this assingment with anyone. 

def park_data():
    park_list=[]
    park_yearly_tourists_list=[]
    park_favorite_thing_list=[]
    parks = 5
    while parks > 0:
        park_name=input('What is one of your favorite Maine parks? ')
        park_list.append(park_name)
        park_yearly_tourists=input(f'How many thousand people visit {park_name} in a year?')
        park_yearly_tourists_list.append(park_yearly_tourists)
        park_favorite_thing=input(f'What is your favorite thing about {park_name}? ')
        park_favorite_thing_list.append(park_favorite_thing)
        parks -= 1
    
    return (park_list , park_yearly_tourists_list, park_favorite_thing_list)
    
park_namelist , park_attendlist , park_favorite_thing_list = park_data()


def celebrate():
    parknumber = int(input('Which park do you want to celebrate (between 0 and 4)?'))
    parknamecel=park_namelist[parknumber]
    attend=int(park_attendlist[parknumber])
    favthing=park_favorite_thing_list[parknumber]
    print(f'At {parknamecel}, I love the: ')
    if (attend <= 10) and (attend < 20):
        print(f'{favthing}!')
    elif attend >=20:
        while (attend >=10):
            print(f'{favthing}!')
            attend -= 10
    


def main():
    
    celebrate()

main()