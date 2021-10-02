import random
import time

board = [' ' for i in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def isWinner(board, letter):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use board instead of board and letter instead of letter so we don’t have to type as much.
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or # across the top
    (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
    (board[1] == letter and board[2] == letter and board[3] == letter) or # across the bottom
    (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
    (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle
    (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
    (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
    (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal

def playerMove():
    flag = True
    while flag:
        move = input("Please select a position to enter an \'X\' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):  # valid move or not
                    flag = False
                    insertLetter('X', move)
                else:
                    print("Position already occupied!")
            else:
                print("Please type a valid number!")
        except:
            print("Please type a number")



def selectRandom(_list):
    return _list[random.randrange(0, len(_list))]
    
def compMove():
    # enumerate all of the empty spaces in board
    possibleMove = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0 
    
    for let in ['O', 'X']:
        for i in possibleMove:
            boardCpy = board[:]
            boardCpy[i] = let  # fill the boardCpy with O and X
            if isWinner(boardCpy, let):  #  check if the current move is winning move
                move = i
                return move

    # try to take the corners
    corners = []
    for i in possibleMove:
        if i in [1, 3, 7, 9]:
            corners.append(i)

    if len(corners) > 0:
        move = selectRandom(corners)
        return move

    # take the center
    if 5 in possibleMove:
        move = 5
        return move

    # take any edge
    edges = []
    for i in possibleMove:
        if i in [2, 4, 6, 8]:
            edges.append(i)
    if len(edges) > 0:
        move = selectRandom(edges)


    return move


    
def isBoardFull(board):
    if board.count(' ') > 1: 
        return False
    else:
        return True

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def main():
    print('Welcome to Tic Tac Toe, to win complete a straight line of your letter (Diagonal, Horizontal, Vertical).\
    The board has positions 1-9 starting at the top left.')
    printBoard(board)
    while not isBoardFull(board):
        if not isWinner(board, 'O'):  # allow the player to play 
            playerMove()
            printBoard(board)
        else:
            print("Dang!! O's won this time")
            break

        if not isWinner(board, 'X'):
            move = compMove()
            if move == 0:
                print("Tie Game")
            else:
                time.sleep(1)
                insertLetter('O', move)
                print("Computer placed an O in postion " + str(move) + " ")
                printBoard(board)
        else:
            print("Whuuhu X won this time")
            break

    if isBoardFull(board):
        print("Tie game")

while True:
    main()
    answer = input("Do you want to play again? (Y/N)")
    if answer.lower() == "y" or answer.lower() == "yes":
        board = [' ' for i in range(10)]
        print("--------------------------------------------")
        main()
    else:
        break

