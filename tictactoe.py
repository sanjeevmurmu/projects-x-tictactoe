"""
Tic Tac Toe Player
"""

from collections import deque
import math
import copy

X = "X"
O = "O"
EMPTY = None
last_five_actions=deque()


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
    totalX=totalO=0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==X:
                totalX+=1
            if board[i][j]==O:
                totalO+=1
    if totalX>totalO:
        return O
    else:
        return X
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    posAction=set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==EMPTY:
                posAction.add((i,j))

    return posAction
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception('Not a valid action')
    
    newBoard = copy.deepcopy(board)
    i,j=action

    curPlayer=player(board)
    newBoard[i][j]=curPlayer
    return newBoard
    # raise NotImplementedError

def result2(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception('Not a valid action')
    
    newBoard = copy.deepcopy(board)
    i,j=action
    last_five_actions.append(action)
    curPlayer=player(board)
    newBoard[i][j]=curPlayer
    
    if len(last_five_actions)>5:
        a,b=last_five_actions.popleft()
        newBoard[a][b]=EMPTY
    return newBoard
    # raise NotImplementedError

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRows(board,X) or checkColumns(board,X) or checkTopBottomDiagonal(board,X) or checkBottomTopDiagonal(board,X): 
        return X
    elif checkRows(board,O) or checkColumns(board,O) or checkTopBottomDiagonal(board,O) or checkBottomTopDiagonal(board,O):
        return O
    else:
        return None
    # raise NotImplementedError        

def checkRows(board,player):
    for row in range(len(board)):    
        count=0
        if board[row][0]==board[row][1]==board[row][2]==player:
            return True

    return False 

def checkColumns(board,player):
    for col in range(len(board[0])):    
        count=0
        if board[0][col]==board[1][col]==board[2][col]==player:
            return True

    return False 
   
def checkTopBottomDiagonal(board,player):
    count=0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if row==col and board[row][col]==player:
                count+=1
    if count==3:
        return True
    else:
        return False

def checkBottomTopDiagonal(board,player):
    count=0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if (len(board)-row-1)==col and board[row][col]==player:
                count+=1
    if count==3:
        return True
    else:
        return False


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    playerWon=winner(board)
    if playerWon is not None:
        return True
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==EMPTY:
                return False
            
    return True
          
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    playerWon=winner(board)
    if playerWon=='X':
        return 1
    elif playerWon=='O':
        return -1
    else:
        return 0
    # raise NotImplementedError



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    curPlayer = player(board)
  

    def maxValue(board):
        v =-math.inf
        bestAction = None
        if terminal(board):
            return utility(board), None
        for action in actions(board):
            minValueResult, _ = minValue(result(board, action))
            if minValueResult > v:
                v = minValueResult
                bestAction = action

            if minValueResult==1:
                break
        return v, bestAction

    def minValue(board):
        v = math.inf
        bestAction = None
        if terminal(board): 
            return utility(board), None
        for action in actions(board):
            maxValueResult, _ = maxValue(result(board, action))
            if maxValueResult < v:
                v = maxValueResult
                bestAction = action
            if maxValueResult==-1:
                break

        return v, bestAction

    if curPlayer == X:
        _, optimal = maxValue(board)
        return optimal
    else:
        _, optimal = minValue(board)
        return optimal
    

