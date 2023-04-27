from enum import IntEnum
# from enum import StrEnum

# If ran, `python3 -O chess.py` then no debug
# If ran, `python3 chess.py` then you get debug prints

class Square:
    def __init__(self, pos_x, pos_y, color, color_emoji, occupied, piece):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.color_emoji = color_emoji
        self.occupied = occupied
        self.piece = piece


class Color(IntEnum):
    WHITE = 0
    BLACK = 1


class SpaceType():
    UNDEFINED   = "\U0001F611"
    WHITE_SPACE = "\U00002B1C"
    BLACK_SPACE = "\U00002B1B"
    WHITE_KING   = "\U00002654"
    WHITE_QUEEN  = "\U00002655"
    WHITE_ROOK   = "\U00002656"
    WHITE_BISHOP = "\U00002657"
    WHITE_KNIGHT = "\U00002658"
    WHITE_PAWN   = "\U00002659"
    BLACK_KING   = "\U0000265A"
    BLACK_QUEEN  = "\U0000265B"
    BLACK_ROOK   = "\U0000265C"
    BLACK_BISHOP = "\U0000265D"
    BLACK_KNIGHT = "\U0000265E"
    BLACK_PAWN   = "\U0000265F"


class Piece():

    in_play = True;
    piece_type = SpaceType.UNDEFINED

    def __init__(self, color=Color.WHITE, pos_x=0, pos_y=0):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def getPieceColor(self):
        return self.color

    def getPosXY(self):
        return (self.pos_x, self.pos_y)

    def getInPlay(self):
        return self.in_play

    def __repr__(self):
        string = str(self.piece_type + " ")
        return f"{string}"


class Pawn(Piece):
    def __init__(self, color=Color.WHITE, pos_x=0, pos_y=0):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hasMoved = False;
        if(color == Color.WHITE):
            self.piece_type = SpaceType.WHITE_PAWN
        else:
            self.piece_type = SpaceType.BLACK_PAWN
    
    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hasMoved = True


class King(Piece):
    def __init__(self, color=Color.WHITE, pos_x=0, pos_y=0):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hasMoved = False;
        if(color == Color.WHITE):
            self.piece_type = SpaceType.WHITE_KING
        else:
            self.piece_type = SpaceType.BLACK_KING
    
    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hasMoved = True

    def isValidMove(self, new_pos_x, new_pos_y):
        
        if(self.isMoveCastle()):
            return True;
        # HERE!!
        return True;

    def isMoveCastle():
        return False;


class Queen(Piece):
    def __init__(self, color=Color.WHITE, pos_x=0, pos_y=0):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        if(color == Color.WHITE):
            self.piece_type = SpaceType.WHITE_QUEEN
        else:
            self.piece_type = SpaceType.BLACK_QUEEN
    
    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


class Rook(Piece):
    def __init__(self, color=Color.WHITE, pos_x=0, pos_y=0):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hasMoved = False;
        if(color == Color.WHITE):
            self.piece_type = SpaceType.WHITE_ROOK
        else:
            self.piece_type = SpaceType.BLACK_ROOK
    
    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hasMoved = True


class Bishop(Piece):
    def __init__(self, color=Color.WHITE, pos_x=0, pos_y=0):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        if(color == Color.WHITE):
            self.piece_type = SpaceType.WHITE_BISHOP
        else:
            self.piece_type = SpaceType.BLACK_BISHOP
    
    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


class Knight(Piece):
    def __init__(self, color=Color.WHITE, pos_x=0, pos_y=0):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        if(color == Color.WHITE):
            self.piece_type = SpaceType.WHITE_KNIGHT
        else:
            self.piece_type = SpaceType.BLACK_KNIGHT
    
    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


class Board:

    turnPlayer = str("White")

    def __init__(self):
        if __debug__:
            print("Hello I am the board")
        
        # each row is A-H
        self.grid = []
        self.grid.append([Rook(Color.WHITE, 0, 0), Knight(Color.WHITE, 1, 0), Bishop(Color.WHITE, 2, 0), King(Color.WHITE, 3, 0), Queen(Color.WHITE, 4, 0), Bishop(Color.WHITE, 5, 0), Knight(Color.WHITE, 6, 0), Rook(Color.WHITE, 7, 0)])
        self.grid.append([Pawn(Color.WHITE, x, 1) for x in range(8)])
        white_black=[SpaceType.WHITE_SPACE, SpaceType.BLACK_SPACE, SpaceType.WHITE_SPACE, SpaceType.BLACK_SPACE, SpaceType.WHITE_SPACE, SpaceType.BLACK_SPACE, SpaceType.WHITE_SPACE, SpaceType.BLACK_SPACE]
        black_white = [SpaceType.BLACK_SPACE, SpaceType.WHITE_SPACE, SpaceType.BLACK_SPACE, SpaceType.WHITE_SPACE, SpaceType.BLACK_SPACE, SpaceType.WHITE_SPACE, SpaceType.BLACK_SPACE, SpaceType.WHITE_SPACE]
        self.grid.append(black_white)        
        self.grid.append(white_black)
        self.grid.append(black_white)        
        self.grid.append(white_black)
        self.grid.append([Pawn(Color.BLACK, x, 6) for x in range(8)])
        self.grid.append([Rook(Color.BLACK, 0, 7), Knight(Color.BLACK, 1, 7), Bishop(Color.BLACK, 2, 7), King(Color.BLACK, 3, 7), Queen(Color.BLACK, 4, 7), Bishop(Color.BLACK, 5, 7), Knight(Color.BLACK, 6, 7), Rook(Color.BLACK, 7, 7)])


    def renderGrid(self):
        column_count = 9
        for row in self.grid[::-1]:
            column_count-=1
            print(column_count, end="")
            for space in row:
                print(space, end="")
            print("")
        print(" A B C D E F G H")

    def isValidSpace():
        return False
    
    def nextMove(self):
        print(self.turnPlayer, "'s move. Please input start and end points.")
        move = str(input())
        # Do some input validation
        splitMove = move.split()
        print(splitMove)
        print(splitMove[0][0])
        if(True):
            # Convert the move string to the positions
            current_pos_x = 0
            current_pos_y = 0
            new_pos_x = 0
            new_pos_y = 0
            if(new_pos_x > 7 or new_pos_x < 0):
                return False
            if(new_pos_y > 7 or new_pos_y < 0):
                return False
        else:
            print("Wrong Input, A1 B2")
    


def printEmptyGrid():
    white_black=[SpaceType.WHITE_SPACE, SpaceType.BLACK_SPACE, SpaceType.WHITE_SPACE, SpaceType.BLACK_SPACE, SpaceType.WHITE_SPACE, SpaceType.BLACK_SPACE, SpaceType.WHITE_SPACE, SpaceType.BLACK_SPACE]
    black_white = [SpaceType.BLACK_SPACE, SpaceType.WHITE_SPACE, SpaceType.BLACK_SPACE, SpaceType.WHITE_SPACE, SpaceType.BLACK_SPACE, SpaceType.WHITE_SPACE, SpaceType.BLACK_SPACE, SpaceType.WHITE_SPACE]
    column_count = 9;
    for y in range(4):
        column_count-=1
        print(column_count, end="")
        for x in white_black:
            print(x, end="")
        column_count-=1
        print("")
        print(column_count, end="")
        for x in black_white:
            print(x, end="")
        print("")
    print("  A B C D E F G H")


def chess():
    board = Board()
    board.renderGrid()
    board.nextMove()


chess()