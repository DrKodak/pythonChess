import chess

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


piece_map = { '0' : "\U00002B1C",
              '1' : "\U00002B1B",
              'K'   : "\U00002654",
              'Q'  : "\U00002655",
              'R'   : "\U00002656",
              'B' : "\U00002657",
              'N' : "\U00002658",
              'P'   : "\U00002659",
              'k'   : "\U0000265A",
              'q'  : "\U0000265B",
              'r'   : "\U0000265C",
              'b' : "\U0000265D",
              'n' : "\U0000265E",
              'p'   : "\U0000265F" 
}

def boardToEmoji(board):
    column_count = 9
    emoji_board = ''
    rows = board.split('/')
    for row in rows:
        emoji_row = []
        for cell in row:
            emoji_row += piece_map[cell]
        print(emoji_row)


def chessLib():
    board = chess.Board()
    print("hello")
    print(board)
    boardToEmoji(board)

chessLib()