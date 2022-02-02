# File:parent_hw2c.py
# Author: Jeffery Parent
# Date: September 23, 2021
# Section: 1006 
# E-mail: Jeffery_parent@maine.edu
# Description:
# Asks user to input bottles used and recycled. gives different outputs depending on users inputs.
# Collaboration:
# I didn't discuss this assingment with anyone.
#

total_used=int(input("Hello, How many bottles/cans did you use today?"))

if total_used > 0 :
    recycled_total=int(input("How many did you recycle?"))

if total_used == 0 :
    print("Great job using no bottles/cans!")
elif recycled_total < total_used and total_used <= 3:
    print("You should recycle more of the bottles you use.")
elif recycled_total == total_used and total_used <= 3:
    print("Nice job recycling all the bottles you used.")
elif recycled_total > total_used and total_used <= 3:
    print("How did you recycle more than you used? Congratulations!")
elif total_used > 3 :
    print("You should get a reusable bottle.")
    if total_used < recycled_total :
            print("Although you recycled more than you used.")

print("Remember to visit the SCIS Help Center in Boardman 138.")
