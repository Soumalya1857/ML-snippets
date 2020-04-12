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
    #raise NotImplementedErrornoX = 0
    noX = 0
    noO = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X: noX += 1
            elif board[i][j] == O: noO += 1
    
    #
    
    if terminal(board) == False:
        #game is not over
        if noX == noO: return X
        elif noX > noO: return O
    else:
        return -1


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #raise NotImplementedError
    if terminal(board) == True:
        return -1
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.add((i,j))
    
    #print(action)
    return action


def result(board,action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #raise NotImplementedError
    i = action[0]
    j = action[1]
    new_board = [[None for m in range(3)] for n in range(3)]
    #print("inside function: "+str(i)+str(j))
    if board[i][j] != None: 
        raise Exception
    for m in range(3):
        for n in range(3):
            new_board[m][n] = board[m][n]
    #new_board = board
    #print(new_board)
    #print(player(new_board))
    if player(new_board) == X: 
        new_board[i][j] = X
        return new_board
    elif player(new_board) == O: 
        new_board[i][j] = O
        return new_board
    #else: raise Exception

    #print(new_board)
    #return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #raise NotImplementedError
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            #print("banchod1")
            #print(i)
            #print("(i,0),(i,1),(i,2)  " + str(board[i][0]) + str(board[i][1]) + str(board[i][2]))
            if board[i][0] == X:
                return X
            elif board[i][0] == O: return O
            #else: continue
    
    for i in range(3):
        if board[0][i] == board[1][i] and board[2][i] == board[1][i]:
            #print("banchod2")
            if board[0][i] == X:
                return X
            elif board[0][i] == O: return O
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        #print("banchod3")
        if board[0][0] == X:
            return X
        elif board[0][0] == O: return O
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
       # print("banchod4")
        if board[0][2] == X:
            return X
        elif board[0][2] == O: return O

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #raise NotImplementedError
    #print(str(winner(board))+"   :winner")
    if winner(board) in [X,O]:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #raise NotImplementedError
    #if terminal(board) == True:
    if winner(board) == X: return 1
    elif winner(board) == O: return -1
    else: return 0
    #else: return None

def maxValue(board):
    if terminal(board) == True or winner(board) == X or winner(board) == O:
        #print(utility(board))
        return utility(board)
    
    v = -500
    temp = -500
    #optimal = ()
    for action in actions(board):
        #print("max: "+ str(action))
        v = max(v,minValue(result(board,action)))
        return v

def minValue(board):
    if terminal(board) or winner(board) == X or winner(board) == O:
        #print(utility(board))
        return utility(board)
    v =  500
    temp = 500
    optimal = ()
    for action in actions(board):
        #print("min: "+ str(action))
        v = min(v,maxValue(result(board,action)))
        return v



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """  
    #print(player(board))  
    #print("player:"+str(player(board)))
    
    maxValueX = -500
    minValueO = 500
    if player(board) == O:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    v = maxValue(board)
                    if v >= maxValueX:
                        maxValueX = v
                        action = (i,j)
        #print(action)
        return action

        
    else: 
        for i in range(3):
            for j in range(3):
                if board[i][j]==EMPTY:
                    v = minValue(board)
                    if v <= minValueO:
                        minValueO = v
                        action = (i,j)
        #print(action)
        return action

    #return v
    #raise NotImplementedError

# def main():
#     #print("shobbai banchod!!!")

#     board = [
#         [X,O,EMPTY],
#         [X,EMPTY,O],
#         [EMPTY,O,X]
#     ]
#     #board = initial_state()
    
#     action = minimax(board)
#     print(action)
#     # print(board)
#     print(result(board,action))

# if __name__ == "__main__":
#     main()