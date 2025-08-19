"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None
    if board == initial_state():
        return X
    if sum(row.count(X) for row in board) > sum(row.count(O) for row in board):
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = deepcopy(board)
    if new_board[action[0]][action[1]] != EMPTY:
        raise ValueError("Invalid move")
    new_board[action[0]][action[1]] = player(new_board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    wins = [
        [(0, 0), (0, 1), (0, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(2, 0), (1, 1), (0, 2)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
    ]
    for [a, b, c] in wins:
        i, j = a
        k, p = b
        m, n = c
        if board[i][j] is not EMPTY and board[i][j] == board[k][p] == board[m][n]:
            return board[i][j]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    if all(cell != EMPTY for row in board for cell in row):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        None
    simulation_board = deepcopy(board)
    if player(simulation_board) == X:
        _, move = max_value(board)
        return move
    else:
        _, move = min_value(board)
        return move


def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board), None
    best_move = None
    for action in actions(board):
        value, _ = min_value(result(board, action))
        if value > v:
            v = value
            best_move = action
    return v, best_move


def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board), None
    for action in actions(board):
        value, _ = max_value(result(board, action))
        if value < v:
            v = value
            best_move = action
    return v, best_move
