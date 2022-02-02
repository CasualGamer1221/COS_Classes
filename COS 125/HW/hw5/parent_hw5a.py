# File:parent_hw5a.py
# Author: Jeffery Parent
# Date: October 22, 2021
# Section: 1006 
# E-mail: Jeffery_parent@maine.edu

# Description:
# Creates a use specified number of slogans from list of words and phrases.

# Collaboration:
# I didn't discuss this assingment with anyone.

import random as rand

def main():
    names = ('Hulk', 'Spock', 'Daenerys', 'Aaron Burr', 'The Cowardly Lion', 'Cinderella',
            'Black Panther', 'Merida', 'Uhuru', 'Freya', 'Frodo', 'Megan Rapinoe')

    verbs = ('Leading', 'Serving', 'Building', 'Creating', 'Putting', 'Fighting', 'Taking',
            'Cleaning up', 'Protecting', 'Putting', 'Smashing', 'Working', 'Incinerating', 'Kicking')

    direct_objects = ('the future', 'our community', ' jobs', 'education', 'corruption',
                    'action', 'families', 'change', 'progress', 'government', 'results', 'our enemies')

    adverb_phrases = ('with integrity', 'for you', 'first', 'safe', 'for the future',
                    'for a change', 'for Maine', ' with experience', ' with vision')

    slogan_number = 0
    slogan_number = int(input('How many slogans should be generated?'))

    while slogan_number > 0:
        print(f"{rand.choice(names)}: {rand.choice(verbs)} {rand.choice(direct_objects)} {rand.choice(adverb_phrases)}")
        slogan_number -= 1
main()