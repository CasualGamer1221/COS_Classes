# File:parent_hw6a.py
# Author: Jeffery Parent
# Date: October 29, 2021
# Section: 1006 
# E-mail: Jeffery_parent@maine.edu

# Description:
# Creates a battleship board with randomly placed ships.

# Collaboration:
# I didn't discuss this assingment with anyone.


import random
random.seed()


def main():
    
    board = [[0 for i in range(10)] for j in range(10)]

    def boardprint():
        for i in board:
            print(' '.join(map(str, i)))
        print()

############################################################################  
    # Ship coordinates
    def shipcoord():
        def random_row(board):
            return random.randint(0, len(board)-1)

        def random_col(board):
            return random.randint(0, len(board[0])-1)

        ship_row = random_row(board)
        ship_col = random_col(board)
        return ship_row, ship_col

############################################################################
    #Ship direction
    def random_dir():
        n = random.randint(1, 4)
        if n == 1:
            return "up"
        elif n == 2:
            return "right"
        elif n == 3:
            return "down"
        elif n == 4:
            return "left"

############################################################################
    # validate the ship can be placed at given coordinates
    def validate(board, ship_row, ship_col, direction, shipsize):
        if direction == "up":
            v = 0
            for i in range(shipsize):
                try:
                    board[ship_row-i][ship_col]
                except IndexError:
                    return False
                if board[ship_row-i][ship_col] > 0:
                    v += 1
            if v >= 1:
                return False
            else:
                return True
        if direction == "right":
            v = 0
            for i in range(shipsize):
                try:
                    board[ship_row][ship_col+i]
                except IndexError:
                    return False
                if board[ship_row][ship_col+i] > 0:
                    v += 1
            if v >= 1:
                return False
            else:
                return True
        if direction == "down":
            v = 0
            for i in range(shipsize):
                try:
                    board[ship_row+i][ship_col]
                except IndexError:
                    return False
                if board[ship_row+i][ship_col] > 0:
                    v += 1
            if v >= 1:
                return False
            else:
                return True
        if direction == "left":
            v = 0
            for i in range(shipsize):
                try:
                    board[ship_row][ship_col-i]
                except IndexError:
                    return False
                if board[ship_row][ship_col-i] > 0:
                    v += 1
            if v >= 1:
                return False
            else:
                return True
    
    #Prints the empty board       
    boardprint()
                  
############################   SHIP PLACEMENT   ################################################
    ### SHIP 2 ###
    while True:
        d = random_dir()  # reset direction
        ship_row, ship_col = shipcoord()
        print('SHIP 2 Coordinates: ', ship_row, ship_col, d)

        if validate(board, ship_row, ship_col, d, 2) == False:
            d = random_dir()
            continue
        if d == "up" and validate(board, ship_row, ship_col, d, 2):
            if ship_row >= 1:
                board[ship_row][ship_col] = 2
                board[ship_row-1][ship_col] = 2
                break
        if d == "right" and validate(board, ship_row, ship_col, d, 2):
            if ship_col <= len(board[0])-2:
                board[ship_row][ship_col] = 2
                board[ship_row][ship_col+1] = 2
                break
        if d == "down" and validate(board, ship_row, ship_col, d, 2):
            if ship_row <= len(board)-2:
                board[ship_row][ship_col] = 2
                board[ship_row+1][ship_col] = 2
                break
        if d == "left" and validate(board, ship_row, ship_col, d, 2):
            if ship_col >= 1:
                board[ship_row][ship_col] = 2
                board[ship_row][ship_col-1] = 2
                break
    print('PLACING PATROL BOAT:')
    boardprint()

    ### SHIP 3.1 ###
    while True:
        d = random_dir()  # reset direction
        ship_row, ship_col = shipcoord()
        print('SHIP 3.1 Coordinates: ', ship_row, ship_col, d)
        if validate(board, ship_row, ship_col, d, 3) == False:
            d = random_dir()
            continue
        if d == "up" and validate(board, ship_row, ship_col, d, 3):
            if ship_row >= 2:
                board[ship_row][ship_col] = 3
                board[ship_row-1][ship_col] = 3
                board[ship_row-2][ship_col] = 3
                break
        if d == "right" and validate(board, ship_row, ship_col, d, 3):
            if ship_col <= len(board[0])-3:
                board[ship_row][ship_col] = 3
                board[ship_row][ship_col+1] = 3
                board[ship_row][ship_col+2] = 3
                break
        if d == "down" and validate(board, ship_row, ship_col, d, 3):
            if ship_row <= len(board)-3:
                board[ship_row][ship_col] = 3
                board[ship_row+1][ship_col] = 3
                board[ship_row+2][ship_col] = 3
                break
        if d == "left" and validate(board, ship_row, ship_col, d, 3):
            if ship_col >= 2:
                board[ship_row][ship_col] = 3
                board[ship_row][ship_col-1] = 3
                board[ship_row][ship_col-2] = 3
                break
    print('PLACING SUBMARINE:')
    boardprint()


### SHIP 3.2 ###
    while True:
        d = random_dir()  # reset direction
        ship_row, ship_col = shipcoord()
        print('SHIP 3.2 Coordinates: ', ship_row, ship_col, d)
        if validate(board, ship_row, ship_col, d, 3) == False:
            d = random_dir()
            continue
        if d == "up" and validate(board, ship_row, ship_col, d, 3):
            if ship_row >= 2:
                board[ship_row][ship_col] = 3
                board[ship_row-1][ship_col] = 3
                board[ship_row-2][ship_col] = 3
                break
        if d == "right" and validate(board, ship_row, ship_col, d, 3):
            if ship_col <= len(board[0])-3:
                board[ship_row][ship_col] = 3
                board[ship_row][ship_col+1] = 3
                board[ship_row][ship_col+2] = 3
                break
        if d == "down" and validate(board, ship_row, ship_col, d, 3):
            if ship_row <= len(board)-3:
                board[ship_row][ship_col] = 3
                board[ship_row+1][ship_col] = 3
                board[ship_row+2][ship_col] = 3
                break
        if d == "left" and validate(board, ship_row, ship_col, d, 3):
            if ship_col >= 2:
                board[ship_row][ship_col] = 3
                board[ship_row][ship_col-1] = 3
                board[ship_row][ship_col-2] = 3
                break
    print('PLACING DESTROYER:')
    boardprint()


### SHIP 4 ###
    while True:
        d = random_dir()  # reset direction
        ship_row, ship_col = shipcoord()
        print('SHIP 4 Coordinates: ', ship_row, ship_col, d)
        if validate(board, ship_row, ship_col, d, 4) == False:
            d = random_dir()
            continue
        if d == "up" and validate(board, ship_row, ship_col, d, 4):
            if ship_row >= 3:
                board[ship_row][ship_col] = 4
                board[ship_row-1][ship_col] = 4
                board[ship_row-2][ship_col] = 4
                board[ship_row-3][ship_col] = 4
                break
        if d == "right" and validate(board, ship_row, ship_col, d, 4):
            if ship_col <= len(board[0])-4:
                board[ship_row][ship_col] = 4
                board[ship_row][ship_col+1] = 4
                board[ship_row][ship_col+2] = 4
                board[ship_row][ship_col+3] = 4
                break
        if d == "down" and validate(board, ship_row, ship_col, d, 4):
            if ship_row <= len(board)-4:
                board[ship_row][ship_col] = 4
                board[ship_row+1][ship_col] = 4
                board[ship_row+2][ship_col] = 4
                board[ship_row+3][ship_col] = 4
                break
        if d == "left" and validate(board, ship_row, ship_col, d, 4):
            if ship_col >= 3:
                board[ship_row][ship_col] = 4
                board[ship_row][ship_col-1] = 4
                board[ship_row][ship_col-2] = 4
                board[ship_row][ship_col-3] = 4
                break
    print('PLACING BATTLESHIP:')
    boardprint()


### SHIP 5 ###
    while True:
        d = random_dir()  # reset direction
        ship_row, ship_col = shipcoord()
        print('SHIP 5 Coordinates: ', ship_row, ship_col, d)
        if validate(board, ship_row, ship_col, d, 5) == False:
            d = random_dir()
            continue
        if d == "up" and validate(board, ship_row, ship_col, d, 5):
            if ship_row >= 4:
                board[ship_row][ship_col] = 5
                board[ship_row-1][ship_col] = 5
                board[ship_row-2][ship_col] = 5
                board[ship_row-3][ship_col] = 5
                board[ship_row-4][ship_col] = 5
                break
        if d == "right" and validate(board, ship_row, ship_col, d, 5):
            if ship_col <= len(board[0])-5:
                board[ship_row][ship_col] = 5
                board[ship_row][ship_col+1] = 5
                board[ship_row][ship_col+2] = 5
                board[ship_row][ship_col+3] = 5
                board[ship_row][ship_col+4] = 5
                break
        if d == "down" and validate(board, ship_row, ship_col, d, 5):
            if ship_row <= len(board)-5:
                board[ship_row][ship_col] = 5
                board[ship_row+1][ship_col] = 5
                board[ship_row+2][ship_col] = 5
                board[ship_row+3][ship_col] = 5
                board[ship_row+4][ship_col] = 5
                break
        if d == "left" and validate(board, ship_row, ship_col, d, 5):
            if ship_col >= 4:
                board[ship_row][ship_col] = 5
                board[ship_row][ship_col-1] = 5
                board[ship_row][ship_col-2] = 5
                board[ship_row][ship_col-3] = 5
                board[ship_row][ship_col-4] = 5
                break
    print('PLACING CARRIER:')
    boardprint()


main()
