"""
A 2-Player TicTacToe Game Script..
Made by:- Ashutosh Muley
"""

import random
import os


# To display the board
def display_board(board):
    """
    input: a board stored as a list
    output: a board in Tabular Format
    """
    i = 7
    print("\n")
    for _ in range(3):
        print("     |     |     ")
        print(f"  {board[i]}  |  {board[i + 1]}  |  {board[i + 2]}  ")
        print("     |     |     ")
        if i != 1:
            print("-" * 17)
        i -= 3
    print("\n")


# To initialize the Markers for players
def player_input():
    '''
    output: return the Markers of the Players as a tuple
    '''
    while True:
        player1 = input("Player1: Please pick a marker 'X' or 'O' :--> ").upper()
        if player1 == 'X' or player1 == 'O':
            break
        else:
            print("Invalid marker choice!! (Choose either 'X' or 'O')")
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return player1, player2


# to place a given marker at a given position on the board
def place_marker(board, marker, position):
    """
    input: a board stored as a list,
           marker to place at the position,
           the position to place the marker
    output: updated board stored as a list
    """
    board[position] = marker
    return board


# To check if a given Mark has won
def win_check(board, mark):
    """
    input: a board stored as a list, marker to check if won
    output: True or False if the Player with the given mark has Won or Not
    """
    # check rows
    i = 1
    for _ in range(3):
        if board[i] == board[i + 1] == board[i + 2] == mark:
            return True
        i += 3
    # check columns

    for i in range(1, 4):
        if board[i] == board[i + 3] == board[i + 6] == mark:
            return True

    # check diagonals
    # right diagonal

    for i in range(1, 10, 4):
        if board[i] != mark:
            break
    else:
        return True
    # left diagonal
    for i in range(3, 8, 2):
        if board[i] != mark:
            break
    else:
        return True

    return False


# To choose the First Player randomly
def choose_first():
    '''
    Randomly choose a player to play first
    '''
    return random.randint(0, 1)


# TO check if a given position on the board is unoccupied
def space_check(board, position):
    '''
    input: a board stored as list, a position on board to check if empty
    output: True or False
    '''
    return board[position] == " "


# To check if the board is full
def full_board_check(board):
    '''
    input: a board stored as a list
    output: True or False if the board is Full or not
    '''
    return " " not in board


# To Allow the Player to choose a position
def player_choice(board):
    '''
    input: a board stored as a list
    output: position chosen by player
    '''
    while True:
        position = input("Enter a position to mark(1-9)->")
        if (not position.isdigit()) or int(position) < 1 or int(position) > 9:
            print("Invalid Position entered!! Enter a No. between 1-9")
        elif space_check(board, int(position)):
            return int(position)
        else:
            print("Invalid Position Space already occupied")


# To Play the game again after a Run
def replay():
    '''
    output: True or False if user wants to replay the game
    '''
    ans = input("Would you like to play again(Yes/No)?")
    return ans.lower()[0] == "y"


# main driver
# print('Welcome to Tic Tac Toe!')
if __name__ == "__main__":
    while True:
        # Set the game up here
        test_board = ['#']
        print('Welcome to Tic Tac Toe!')
        for _ in range(9):
            test_board.append(" ")
        display_board(test_board)
        player = player_input()
        first = choose_first()
        if first == 0:
            second = 1
        else:
            second = 0
        p1 = False
        p2 = False

        while not full_board_check(test_board):
            # Player 1 Turn
            print(f"\nPlayer {first + 1}'s Turn: ")
            position = player_choice(test_board)
            test_board = place_marker(test_board, player[first], position)
            os.system('clear')
            display_board(test_board)
            if win_check(test_board, player[first]):
                p1 = True
                break
            if full_board_check(test_board):
                break
            # Player2's turn.
            print(f"\nPlayer {second + 1}'s Turn: ")
            position = player_choice(test_board)
            test_board = place_marker(test_board, player[second], position)
            os.system('clear')
            display_board(test_board)
            if win_check(test_board, player[second]):
                p2 = True
                break
            if full_board_check(test_board):
                break

        if p1 == True:
            print('\n', f"Player {first + 1} wins!!!".center(45, '*'))
        elif p2 == True:
            print("\n", f"Player {second + 1} wins!!!".center(45, '*'))
        else:
            print("\n", "Its a TIE".center(45, '*'))

        if not replay():
            os.system('clear')
            break
        os.system('clear')
