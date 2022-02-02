################################
# LAB 11
# Agent in 2d environ simulator
# By zsh
# Uses the graphics.py from Zelle
#   https://mcsp.wartburg.edu/zelle/python/graphics.py
################################

from graphics import *
import random

# Random seed. If you want to see the same map over and over
#   set this to an integer value.
SEED = None

INT_GOAL = 2
INT_OPEN = 0
INT_OBSTACLE = 1
INT_PATH = 8
INT_OFFMAP = 9

# Cell values into which the agent can move. Use this:
#   if cells[x][y] in VALID_MOVES:
VALID_MOVES = [0,2,8]

# Valid directions.
N = (0,-1)
E = (1,0)
W = (-1,0)
S = (0,1)
NE = (1,-1)
NW = (-1,-1)
SE = (1,1)
SW = (-1,1)
DIRS = [
    N, S, E, W, NE, NW, SE, SW
]
##############################################################################
##############################################################################
##############################################################################
##############################################################################
# Your AI goes in this function: GetMove. It must return one of the directions above.
# Else stuff will crash. Warned. The directions are not board locations
# but changes in x,y.
#
# You are free to make other functions which this function calls.
#
# By default, the AI is a random walk. Meaning, it randomly chooses a direction
# without looking if it's valid. You should do something more intelligent.
#
# The program will check if the move is valid or not, so even if your AI
# picks an invalid cell (obstacle), the agent won't move.
#
# PARAMS:
#   player: a list with the x,y location of the player. player[0]=x. player[1]=y
#   cells: a 3x3 list of the board cells surrounding the player.
#   goal: a list (like player) with the x,y location of the goal.
# RETURN:
#   must return an x,y change. Each x and y must be in [-1,0,1]
#   If you return (0,0), this indicates your AI has decided there are no
#   valid moves and the program quits.
def GetMove(player, cells, goal):
    # print(player)
    PrintBoard(cells)
    x=None
    y=None
    
    if (player[0]-goal[0]) != 0: 
        x= ((player[0]-goal[0])//abs(player[0]-goal[0]))
    else: x=0
    
    if (player[1]-goal[1]) != 0: 
        y=((player[1]-goal[1])//abs(player[1]-goal[1]))
    else: y=0
    
    
    if x==(1):
        ls=(3,5,7)
        return DIRS[random.choice(ls)]
    elif x==(-1):
        ls1=(2,4,6)
        return DIRS[random.choice(ls1)]
    elif y==(1):
        ls2=(0,4,5)
        return DIRS[random.choice(ls2)]
    elif y==(-1):
        ls3=(1,6,7)
        return DIRS[random.choice(ls3)]
    else:
        return random.choice(DIRS)

##############################################################################
##############################################################################
##############################################################################


# Make a window
def CreateWindow(width, height):
    win = GraphWin("Maze", width, height)
    return win

# Draws everything
def DrawBoard(win, board, player,goal):

    w = win.getWidth()
    h = win.getHeight()

    cell_size = (w-20)/len(board)

    for x in range(len(board)+1):
        l = Line(Point(x*cell_size+10,10),Point(x*cell_size+10,h-10))
        l.draw(win)
    
    for y in range(len(board[0])+1):
        l = Line(Point(10,y*cell_size+10),Point(w-10,y*cell_size+10))
        l.draw(win)

    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y]==INT_OBSTACLE:
                r = Rectangle(
                        Point(x*cell_size+10,y*cell_size+10),
                        Point(x*cell_size+10+cell_size,y*cell_size+10+cell_size)
                    )
                r.setFill('gray')
                r.draw(win)
            
            
            elif board[x][y]==INT_PATH:
                c = Circle(
                    Point(x*cell_size+10+cell_size/2, y*cell_size+10+cell_size/2),
                    3
                )
                c.setFill('red')
                c.draw(win)


    r = Rectangle(
            Point(goal[0]*cell_size+10,goal[1]*cell_size+10),
            Point(goal[0]*cell_size+10+cell_size,goal[1]*cell_size+10+cell_size)
        )
    r.setFill('green')
    r.draw(win)


    playerchar = Circle(
        Point(player[0]*cell_size+10+cell_size/2, player[1]*cell_size+10+cell_size/2),
        cell_size//2-2
    )
    playerchar.setFill('blue')
    playerchar.draw(win)

    return playerchar

# Gens obstacles
def CreateObstacles(board, oper):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if random.random() < oper:
                board[x][y] = INT_OBSTACLE

    for x in range(len(board)):
        board[x][0]=INT_OBSTACLE
        board[x][len(board[0])-1]=INT_OBSTACLE
    for y in range(len(board)):
        board[0][y]=INT_OBSTACLE
        board[len(board[0])-1][y]=INT_OBSTACLE

# Looks around for an empty spot.
# If you set the obstacle percent too high this might take forever.
def FindEmptySpot(board):
    while True:
        row = random.randrange(len(board))
        if sum(board[row])==len(board):
            continue
        else:
            while True:
                col = random.randrange(len(board[row]))
                if board[row][col]==INT_OPEN:
                    return [row,col]

# Convenience functions to make the player and goal locs
def CreateGoal(board):
    goal =  FindEmptySpot(board)
    board[goal[0]][goal[1]] = INT_GOAL
    return goal
def CreatePlayer(board):
    return FindEmptySpot(board)
    
def PrintBoard(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            print(board[y][x],end=' ')
        print()

# Gets the 3x3 slice of the board around the player
def GetBoardSlice(board,player,agent_sight):
    radius = 1+agent_sight*2
    s = []
    for x in range(radius):
        row = []
        for y in range(radius):
            row.append(INT_OFFMAP)
        s.append(row)

    for x in range(radius):
        for y in range(radius):
            nx = x-agent_sight+player[0]
            ny = y-agent_sight+player[1]
            if nx>=0 and ny>=0 and nx<len(board) and ny<len(board[0]):
                s[x][y] = board[nx][ny]
            
    return s

# Checks if the move requested by the AI is valid.
def TestMove(move, player, board):
    if abs(move[0]) > 1 or abs(move[1])>1:
        return False
    x = move[0]+player[0]
    y = move[1]+player[1]
    if board[x][y] in VALID_MOVES:
        return True
    else:
        return False

# Checks for wins.
def CheckWin(player,goal):
    if player==goal:
        return True
    else:
        return False

# Convenience function to catch Escape.
def GetInput(win):
    if win.getKey()=="Escape":
        return False
    return True

# Main loop.
#   - Keeps looping until player==goal or user hits Escape
def Loop(board,player,win,goal,agent_sight):

    run = True

    # First draw, so we can see starting position
    playerchar = DrawBoard(win,board,player,goal)
    win.getKey()
    if playerchar:
            playerchar.undraw()

    # Actual loop
    while run:

        # Get the board slice and move from the player
        board_slice = GetBoardSlice(board,player,agent_sight)
        move = GetMove(tuple(player), board_slice,tuple(goal))

        if move==(0,0):
            run=False
            continue

        # If the move is legit, mark current loc in board and move
        if TestMove(move,player,board):
            board[player[0]][player[1]]=INT_PATH
            player[0]+=move[0]
            player[1]+=move[1]

        # Draw the new situation
        playerchar = DrawBoard(win,board,player,goal)

        # Did we win yet?
        if CheckWin(player,goal):
            win_text = Text(Point(win.getWidth()//2,win.getHeight()//2),"AI WINS")
            win_text.setSize(30)
            win_text.draw(win)
            win.getKey()
            run = False

        # See if user hit Escape
        if run and not GetInput(win):
            run = False

        # Delete player from board
        elif playerchar:
            playerchar.undraw()

        
# Ye Olde Maine
def main():

    random.seed(SEED)

    # Vars and defs
    wwidth = 600            # Window width
    wheight = 600           # Window height
    bwidth = 10             # Board width
    bheight = 10            # Board height
    obstacle_percent = 0.1  # Percent a cell is an obstacle
    player = [0,0]          # player location
    board = []              # The board
    agent_sight = 1         # How many cells the agent sees

    # Make 2d board list
    for x in range(bwidth):
        row = []
        for y in range(bheight):
            row.append(0)
        board.append(row)
    
    # Create the obstacles
    CreateObstacles(board,obstacle_percent)

    # Set the goal and player
    goal = CreateGoal(board)
    player = CreatePlayer(board)

    # Create the win
    win = CreateWindow(wwidth,wheight)

    # Kick it
    Loop(board,player,win,goal,agent_sight)

    # Done and done
    win.close()



main()