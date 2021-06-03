"""
Tic Tac Toe Player
"""

import math
import copy

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

    num_of_x = 0
    num_of_o = 0

    for row in board:
        num_of_x += row.count(X)
        num_of_o += row.count(O)

    return X if num_of_x == num_of_o else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    new_board = copy.deepcopy(board)
    i, j = action
    mark = player(board)

    new_board[i][j] = mark

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for mark in [X, O]:

        for row in range(0, 3):
            if all(board[row][col] == mark for col in range(0, 3)):
                return mark

        for col in range(0, 3):
            if all(board[row][col] == mark for row in range(0, 3)):
                return mark

        for diagonal in [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]:
            if all(board[row][col] == mark for (row, col) in diagonal):
                return mark

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if all(EMPTY not in row for row in board):
        return True

    return winner(board) is not None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    winner_mark = winner(board)
    mark_to_utility = {X: 1, O: -1, None: 0}

    return mark_to_utility[winner_mark]


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def min_value(board):
        if terminal(board):
            return utility(board)

        v = math.inf
        for move in actions(board):
            v = min(v, max_value(result(board, move)))

        return v

    def max_value(board):
        if terminal(board):
            return utility(board)

        v = -math.inf
        for move in actions(board):
            v = max(v, min_value(result(board, move)))

        return v

    if terminal(board):
        return None

    if player(board) == X:
        best_v = -math.inf

        for move in actions(board):
            max_v = min_value(result(board, move))

            if max_v > best_v:
                best_v = max_v
                best_move = move

    else:
        best_v = math.inf

        for move in actions(board):
            min_v = max_value(result(board, move))

            if min_v < best_v:
                best_v = min_v
                best_move = move

    return best_move
