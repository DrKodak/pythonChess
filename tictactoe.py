# Globals
EMPTY_SPOT = '\U00002B1C'
CIRCLE = '\U00002B55'
CROSS = '\U0000274C'
CROSSED_SWORDS = '\U00002694'

EMPTY_BOX = '\U0001F532'

BOX_1 = '1️⃣'
BOX_2 = '2️⃣'
BOX_3 = '3️⃣'
BOX_4 = '4️⃣'
BOX_5 = '5️⃣'
BOX_6 = '6️⃣'
BOX_7 = '7️⃣'
BOX_8 = '8️⃣'
BOX_9 = '9️⃣'


def placeInSpot(grid, x, y, emoji):
    grid[x][y] = emoji
    return grid

def printGrid(grid):
    for row in grid:
        for cell in row:
            if(cell == EMPTY_SPOT):
                item= EMPTY_SPOT
            elif(cell == 'X'):
                item = CROSS
            else:
                item = CIRCLE
            print(item, end='')
        print("")

def startingGrid():
    empty_grid = []
    for x in range(3):
        row = []
        for y in range(3):
            row.append(EMPTY_SPOT)
        empty_grid.append(row)
    return empty_grid


def numberedGrid():
    empty_grid=[]
    empty_grid.append([BOX_1, BOX_2, BOX_3])
    empty_grid.append([BOX_4, BOX_5, BOX_6])
    empty_grid.append([BOX_7, BOX_8, BOX_9])
    return empty_grid

def turn(grid, TURN_PLAYER):
    valid_move = False
    while(not valid_move):
        move = str(input(TURN_PLAYER + " please input move: "))
        xy = move.lstrip().rstrip().split(' ')
        x = int(xy[0]) 
        y = int(xy[1])
        if(grid[x][y] == 'X' or grid[x][y] == 'O'):
            print("Invalid Move!")
            continue
        valid_move = True
    grid = placeInSpot(grid, x, y, TURN_PLAYER)

    return grid

def checkTurnPlayer(grid):
    # determine the number of spaces occupied
    count = 0
    for row in grid:
        for cell in row:
            if(cell != EMPTY_SPOT):
                count+=1
    if(count == 0):
        return 'X'
    elif(count % 2 == 0):
        return 'X'
    else:
        return 'O'
    
def checkWin(grid):
    # return 0 for continue
    # return 1 for X win
    # return 2 for O win
    # return 3 for draw
    return_code = 0

    # Check the rows
    if(grid[0][0] == grid[1][0] == grid[2][0] == 'X'):
        return 1
    if(grid[0][1] == grid[1][1] == grid[2][1] == 'X'):
        return 1
    if(grid[0][2] == grid[1][2] == grid[2][2] == 'X'):
        return 1
    
    if(grid[0][0] == grid[1][0] == grid[2][0] == 'O'):
        return 2
    if(grid[0][1] == grid[1][1] == grid[2][1] == 'O'):
        return 2
    if(grid[0][2] == grid[1][2] == grid[2][2] == 'O'):
        return 2
    
    # Check the cols
    if(grid[0][0] == grid[1][0] == grid[2][0] == 'X'):
        return 1
    if(grid[0][1] == grid[1][1] == grid[2][1] == 'X'):
        return 1
    if(grid[0][2] == grid[1][2] == grid[2][2] == 'X'):
        return 1
    
    if(grid[0][0] == grid[1][0] == grid[2][0] == 'O'):
        return 2
    if(grid[0][1] == grid[1][1] == grid[2][1] == 'O'):
        return 2
    if(grid[0][2] == grid[1][2] == grid[2][2] == 'O'):
        return 2

    # Check the diags
    if(grid[0][0] == grid[1][1] == grid[2][2] == 'X'):
        return 1
    if(grid[0][2] == grid[1][1] == grid[2][0] == 'X'):
        return 1
    if(grid[0][0] == grid[1][1] == grid[2][2] == 'O'):
        return 2
    if(grid[0][2] == grid[1][1] == grid[2][0] == 'O'):
        return 2

    # Do the Draw condition
    

    return 0

def game():
    # X goes first
    TURN_PLAYER = 'X'
    grid = startingGrid()
    printGrid(grid)
    check = 0
    while(check == 0):
        # just do 3 turns
        grid = turn(grid, TURN_PLAYER)
        printGrid(grid)
        check = checkWin(grid)
        if(check==0):
            TURN_PLAYER = checkTurnPlayer(grid)
    if(check == 1):
        print("Congrats X!")
    if(check == 2):
        print("Congrats O!")
    if(check == 3):
        print("Draw!")

game()