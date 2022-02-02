# File:parent_hw5c.py
# Author: Jeffery Parent
# Date: October 22, 2021
# Section: 1006 
# E-mail: Jeffery_parent@maine.edu

# Description:
# 

# Collaboration:
# I didn't discuss this assingment with anyone.

import random as rand

def main():
    
    player1=input("player 1 name: ")
    player2=input("player 2 name: ")

    player1_score=0
    player2_score=0

    player =1
    
    
    
    if player == 1:
        rollvalue = 1
        print(f'{player1.capitalize()}\'s turn')
        while player1_score < 20:
            die_value=rand.randrange(1,7)
            if die_value == 1:
                print(f'Roll {rollvalue} Value: {die_value}')
                player1_score=0
                break
            player1_score += die_value
            print(f'Roll {rollvalue} Value: {die_value}')
            rollvalue+=1
        print(f'{player1.capitalize()}\'s score: {player1_score}')
        print()
        player += 1
        
    if player == 2:
        rollvalue = 1
        print(f'{player2.capitalize()}\'s turn')
        while player2_score < 20:
            die_value=rand.randrange(1,7)
            if die_value == 1:
                print(f'Roll {rollvalue} Value: {die_value}')
                player2_score=0
                break
            player2_score += die_value
            print(f'Roll {rollvalue} Value: {die_value}')
            rollvalue+=1
        print(f'{player2.capitalize()}\'s score: {player2_score}')
        print()
        player -=1 

    if player1_score < player2_score:
        print(f'{player2.capitalize()} wins!!')
    elif player1_score > player2_score:
        print(f'{player1.capitalize()} wins!!')
    elif player1_score == player2_score:
        print("You are tied with each other.")
    else:
        print("Did you even play??")
    


main()