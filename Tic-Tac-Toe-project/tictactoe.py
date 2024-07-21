"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    CountX = 0
    CountO = 0

    for row in board:
        CountX += row.count(X)
        CountO += row.count(O)

    if CountX <= CountO:
        return CountX
    else:
        return CountO


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()

    for row_index, row in enumerate(board):
        for column_index, item in enumerate(row):
            if item == None:
                moves.add((row_index, column_index))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_move = player(board)

    new_board = deepcopy(board)
    i, j = action
    if board[i][j] != None:
        return Exception
    else:
        new_board = board[i][j]

    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # horizontal
    for i in range(3):
        column = [board[x][i] for x in range(3)]
        if column == [player] * 3:
            return player
    
    #vertical
    for row in board:
        if row == [player] * 3:
            return player
        
    #diagonal
    #left
    if board[0][0] == board[1][1] == board[2][2] !="_":
        return player
    #right
    if board[0][2] == board[1][1] == board[2][0] !="_":
        return player


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #we got a winner
    if winner(board) !=None:
        return True

    #still empty cell
    for row in board:
        if EMPTY in row:
            return False
    
    #no more moves
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner = winner(board)
    if winner == X:
        return 1
    elif winner == O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
