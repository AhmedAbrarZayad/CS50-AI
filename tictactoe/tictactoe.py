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
    o = 0
    x = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] is X:
                x+=1
            elif board[i][j] is O:
                o+=1
    if x+o == 9:
        return 0
    elif x > o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                action.add((i,j))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    deep_copy = copy.deepcopy(board)
    if action is None:
        return board
    if deep_copy[action[0]][action[1]] is not EMPTY:
        raise ValueError
    if player(board) is O:
        deep_copy[action[0]][action[1]] = O
    elif player(board) is X:
        deep_copy[action[0]][action[1]] = X
    return deep_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        x = 0
        o = 0
        for j in range(3):
            x = x + (board[i][j] == X)
            o = o + (board[i][j] == O)
        if x == 3:
            return X
        elif o == 3:
            return O
    for i in range(3):
        x = 0
        o = 0
        for j in range(3):
            x = x + (board[j][i] == X)
            o = o + (board[j][i] == O)
        if x == 3:
            return X
        elif o == 3:
            return O
    x = 0
    o = 0
    for i in range(3):
        x = x + (board[i][i] == X)
        o = o + (board[i][i] == O)
    if x == 3:
        return X
    elif o == 3:
        return O
    x = 0
    o = 0
    j = 2
    for i in range(3):
        x = x + (board[i][j] == X)
        o = o + (board[i][j] == O)
        j-=1   
    if x == 3:
        return X
    elif o == 3:
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] is EMPTY:
                    return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) is X:
        return 1
    elif winner(board) is O:
        return -1
    elif terminal(board) is True:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) is True:
        return None
    else:
        actionsForAI = actions(board)
        ind = 0
        if player(board) is X:
            ind = -2
        elif player(board) is O:
            ind = 2
        ans = None
        for action in actionsForAI:
            copy_board = result(board, action)
            while terminal(copy_board) is False:
                copy_board = result(copy_board, minimax(copy_board))
            if player(board) is X:
                if utility(copy_board) == 1:
                    return action
                elif ind < utility(copy_board):
                    ind = utility(copy_board)
                    ans = action
            elif player(board) is O:
                if utility(copy_board) == -1:
                    return action
                elif ind > utility(copy_board):
                    ind = utility(copy_board)
                    ans = action
            
        return ans