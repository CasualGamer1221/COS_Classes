# File:parent_hw3c.py
# Author: Jeffery Parent
# Date: October 8, 2021
# Section: 1006 
# E-mail: Jeffery_parent@maine.edu

# Description:
# Prints a list of animals with index.
# Collaboration:
# I didn't discuss this assingment with anyone.


def main():
   
    listanimals = [
        "Aardvark", "Albatross", "Alligator", "Alpaca", "Ant", "Anteater", "Antelope", "Ape", "Armadillo", "Donkey", "Baboon", "Badger", "Barracuda", "Bat", "Bear", "Beaver", "Bee",
        "Bison", "Boar", "Buffalo", "Butterfly", "Camel", "Capybara", "Caribou", "Cassowary", "Cat", "Caterpillar", "Cattle", "Chamois", "Cheetah", "Chicken", "Chimpanzee", "Chinchilla", "Chough", "Clam",
        "Cobra", "Cockroach", "Cod", "Cormorant", "Coyote", "Crab", "Crane", "Crocodile", "Crow", "Curlew", "Deer", "Dinosaur", "Dog", "Dogfish", "Dolphin", "Dotterel", "Dove", "Dragonfly", "Duck", "Dugong",    "Dunlin",    "Eagle",    "Echidna",
        "Eel",   "Eland",   "Elephant",    "Elk",    "Emu",    "Falcon",    "Ferret",    "Finch", "Fish", "Flamingo", "Fly", "Fox", "Frog", "Gaur", "Gazelle", "Gerbil", "Giraffe", "Gnat", "Gnu", "Goat", "Goldfinch", "Goldfish", "Goose", "Gorilla",
        "Goshawk", "Grasshopper", "Grouse", "Guanaco", "Gull", "Hamster", "Hare", "Hawk", "Hedgehog", "Heron", "Herring", "Jaguar", "Jay", "Jellyfish", "Kangaroo", "Kingfisher", "Koala", "Leopard", "Lion", "Llama", "Lobster",
        "Locust", "Loris", "Louse", "Lyrebird", "Magpie", "Mallard", "Mongoose", "Monkey", "Moose", "Mosquito", "Mouse", "Mule", "Narwhal", "Otter", "Owl", "Oyster", "Panther", "Parrot", "Partridge", "Peafowl", "Pelican",
        "Raccoon", "Rail", "Ram", "Rat", "Raven", "Red deer", "Red panda", "Skunk", "Snail", "Snake", "Sparrow", "Spider", "Spoonbill", "Squid", "Squirrel", "Starling", "Stingray", "Stinkbug", "Stork", "Swallow", "Swan", "Tapir", "Tarsier", "Termite", "Tiger", "Toad", "Trout",
        "Wombat",  "Woodcock",  "Woodpecker",  "Worm",  "Wren",  "Yak",  "Zebra"]

    for i in range(len(listanimals)):
        print((i+1),":" , listanimals[i])
    
    
main()