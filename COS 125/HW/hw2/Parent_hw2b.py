# File:parent_hw2b.py
# Author: Jeffery Parent
# Date: September 23, 2021
# Section: 1006 
# E-mail: Jeffery_parent@maine.edu
# Description:
# asks the user for different grades and their weight. then prints out the class grade.
# Collaboration:
# I didn't discuss this assingment with anyone.
#
#

print("Hello, I will calculate your grade.")
Homework_weight=float(input("What is the homework weight?"))
Homework_grade=float(input("What is your homework grade?"))
Project_weight=float(input("What is the project weight?"))
Project_grade=float(input("What is your project grade?"))
Engagement_Activities_Weight=float(input("What is the engagement activities weight?"))
Engagement_Activities_Grade=float(input("What is your engagement grade?"))
Lab_Weight=float(input("What is the lab weight?"))
Lab_Grade=float(input("What is your lab grade?"))
Hourly_Exam_Weight=float(input("What is the hourly exam weight?"))
Hourly_Exam_Grade=float(input("What is your hourly exam grade?"))
Final_Exam_Weight=float(input("What is the final exam weight?"))
Final_Exam_Grade=float(input("What is your final exam grade?"))

Homework_grade=Homework_grade*Homework_weight
Project_grade=Project_grade*Project_weight
Engagement_Activities_Grade=Engagement_Activities_Grade*Engagement_Activities_Weight
Lab_Grade=Lab_Grade*Lab_Weight
Hourly_Exam_Grade=Hourly_Exam_Grade*Hourly_Exam_Weight
Final_Exam_Grade=Final_Exam_Grade*Final_Exam_Weight

total_grade=Homework_grade+Project_grade+Engagement_Activities_Grade+Lab_Grade+Hourly_Exam_Grade+Final_Exam_Grade
print("Your grade is,", total_grade,".")