# File:parent_Project2.py
# Author: Jeffery Parent
# Date: December 9, 2021
# Section: 1006 
# E-mail: Jeffery_parent@maine.edu
# Description:
# Creates a Lindenmeyer system using a user inputted angle, grammar, and iteration count

# Collaboration:
# I didn't discuss this assingment with anyone.
############################################################################

from graphics import *
import math
import random as rand
############################################################################

# Find the next point given the previous point, an angle, and a distance.
def find_next_point(point, angle, distance):
    x = point.getX()
    y = point.getY()
    return Point(x + (math.cos(angle) * distance), y + (math.sin(angle) * distance))

############################################################################
# Creates a list containing the grammar rules.
def grammar():
    file = open(input("Input filename containing grammar: ")) 
    lines = file.readlines()
    grammar_list = []
    for line in lines:
        grammar_list.append(line.strip())
    return grammar_list

################################################################################
# Creates a list containing the grammar rules.
def apply_rules(letter, grammar_list):
    # Apply rules to an individual letter, and return the result.
    if letter == 'X':
        new_string = grammar_list[1][2:]
    elif letter == 'F':
        new_string = grammar_list[2][2:]
    else:
        new_string = letter
    return new_string

################################################################################
# Creates a new string by putting the previous generation string through the apply_rules() function.
def process_string(original_string, grammar_list):
    transformed_string = ""
    for letter in original_string:
        transformed_string = transformed_string + apply_rules(letter, grammar_list)
    return transformed_string

################################################################################
# Begin with an axiom, and apply rules to the original axiom string number_of_iterations times, then return the result.
def create_l_system(number_of_iterations, axiom, grammar_list):
    start_string = axiom
    if number_of_iterations == 0:
        return start_string
    else:
        for i in range(number_of_iterations):
            end_string = process_string(start_string, grammar_list)
            start_string = end_string
        return end_string
    
################################################################################
# Graphs the L-system from the generated string.
def graph(angle, number_of_iterations, axiom, grammar_list):
    # Sets the graph background and size
    window_height = 800 ; window_length = 800
    win = GraphWin("My Drawing", window_length, window_height)
    win.setBackground(color_rgb(245,241,128))       

    line_length = 17 // (number_of_iterations**0.5)
    ################################################################################
    # Sets graph coordianates to different amounts based on given angle and number of iterations.
    if number_of_iterations <= 4:
        if angle > math.radians(50):
            max_x_coord = 200*(number_of_iterations**0.6) ; max_y_coord = 200*(number_of_iterations**0.4)
        else:
            max_x_coord = 200*(number_of_iterations**0.4) ; max_y_coord = 200*(number_of_iterations**0.5)
    elif (number_of_iterations > 4) and (number_of_iterations < 8):
        if angle > math.radians(50):
            max_x_coord = 600*(number_of_iterations**0.8) ; max_y_coord = 500*(number_of_iterations**0.7)
        else:
            max_x_coord = 500*(number_of_iterations**0.7) ; max_y_coord = 500*(number_of_iterations**0.9)
    elif number_of_iterations >= 8:
        if angle > math.radians(50):
            max_x_coord = 1000*number_of_iterations ; max_y_coord = 800*number_of_iterations
        else:
            max_x_coord = 800*number_of_iterations ; max_y_coord = 1000*number_of_iterations
   
    win.setCoords(0,0,max_x_coord,max_y_coord)
    ################################################################################
    # Gets the L-system string.
    for i in range(number_of_iterations):
        l_system_string = create_l_system(number_of_iterations, axiom, grammar_list)
        
    #list of saved coordinates and angles at opening brackets("[")
    coordinate_stack=[] 
    angle_stack=[]
    
    # sets a starting coordinate and a last_coord that changes based on where the line ends.
    start_coord = Point(max_x_coord//2 , max_y_coord//10)
    last_coord = start_coord
    angle2 = math.radians(90)
        
    ################################################################################
    # Graphs the L-system as it iterates through the string.
    for i in l_system_string:
        if i == "F":
            aLine= Line(last_coord,find_next_point(last_coord, angle2 , line_length))
            last_coord = aLine.getP2()
            aLine.setOutline("black")
            aLine.setWidth(1)
            aLine.draw(win)
            
        if i == "X":
            continue
        
        elif i == "[":
            coordinate_stack.append(last_coord)
            angle_stack.append(angle2)
            
        elif i == "]":
            last_coord=coordinate_stack.pop()
            angle2=angle_stack.pop()
            
        elif i == "+":
            angle2 -= angle
        
        elif i == "-":
            angle2 += angle
      
        else: continue
    win.getMouse() 

################################################################################

def main():
    
    number_of_iterations = int(input("iterations? "))
    angle = math.radians(float(input("What angle do you want? ")))
    grammar_list = grammar()
    axiom = grammar_list[0]
    
    graph(angle, number_of_iterations, axiom, grammar_list)
main()
            