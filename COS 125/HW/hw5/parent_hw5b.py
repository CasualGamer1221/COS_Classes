# File:parent_hw5b.py
# Author: Jeffery Parent
# Date: October 22, 2021
# Section: 1006
# E-mail: Jeffery_parent@maine.edu

# Description:
# prints a palidrome from a user defined word using the minimum number of characters possible.
# if the word is already a palindrome, the user is notified.
# if the input is more than one word, then a space must be inserted after the last word.
# Collaboration:
# I didn't discuss this assingment with anyone.


def main():
    string1 = ''
    while string1 != "quit":
        string1 = input("Enter a string that you would like to palindromize (enter \"quit\" to exit): ")

        if string1 == "quit":  # quits function
            break
        else:
            string2 = string1[::-1]  # reverses string1 and saves as string2

            # Removes last letter of string1 and first letter of string2 if they are equal, until they are different.
            if string1 != string2:
                while (string1[-1]) == (string2[0]):
                    string2 = string2[1:]
                print(string1+string2)
            else:
                print(f'Your word \"{string1}\" is already a palindrome!')


main()
