# # # The aim of this project is to create a two player game of tic tac to
# # # first asks if you want to play
# # What do you want to be x or o
# # You place your thing on the grid by typing an assigned number on the keyboard
# # tell you when u win
#

# function which defines and displays the board
def display_board(board):
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

# Function in order to decide what marker the plaer is

def player_input():
    marker = " "

    # while marker != "X" or marker != "O":
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1 do you want to play as X or O ').upper()

    if marker == "X":
        return ('X', 'O')
    else:
        return ('O', 'X')

# Function to put the marker on the board

def place_marker(board, marker, position):
    board[position] = marker

# Function to see if player has won or not:

def win_check(board, mark):
    result = 0
    for q in range(0, 7, 3):
        if board[q] == mark and board[q + 1] == mark and board[q + 2] == mark:
            result += 1

    for a in range(0, 3):
        if board[a] == mark and board[a + 3] == mark and board[a + 3] == mark:
            result += 1

    for c in range(0, 3, 2):
        if board[c] == mark and board[c + 2] == mark and board[c + 4] == mark:
            result += 1

    return result > 0

# to see if its a tie or not:
def tie_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
# in order to see if the tile is empty or not

def space_check(board, position):
    return board[position] == " "

#function to see if the board is full or not

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position

# who goes first

import  random
def choose_turn():
    if random.random() > 0.5:
        return "Player 1"
    else:
        return "Player 2"
# putting all the function together

print('Welcome to Tic Tac Toe!')
while True:
    game_board = [" "] * 10

    player1_marker, player2_marker = player_input() #tuple value

    turn = choose_turn()
    print(turn + ' will go first.')

    play_game = input("Are you ready to play? Enter Yes or No. ")

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
# player 1 turn

        display_board(game_board)
        position = player_choice(game_board)
        place_marker(game_board, player1_marker, position)


        if win_check(game_board, player1_marker):
            display_board(game_board)
            print('Congratulations! You have won the game!')
            game_on = False
        else:
            if tie_check(game_board):
                display_board(game_board)
                print('The game is a draw!')
                break
            else:
                turn = 'Player 2'

    # player 2's turn

        display_board(game_board)
        position = player_choice(game_board)
        place_marker(game_board, player2_marker, position)

        if win_check(game_board, player2_marker):
            display_board(game_board)
            print('Player 2 has won!')
            game_on = False
        else:
            if tie_check(game_board):
                display_board(game_board)
                print('The game is a draw!')
                break
            else:
                turn = 'Player 1'


# #1. build the grid
#
# board1 = [1, 2, 3]
# board2 = [4, 5, 6]
# board3 = [7, 8, 9]
#
# def print_the_board():
#     print(board1)
#     print(board2)
#     print(board3)
#
# # #2. Do you want to play the game
#
# flag = input("Do you want to play Tic Tac To? (yes or no) ")
# print(flag)
#
# # #3.choose x or o
#
# if flag == "yes":
#     choose = input("Player 1: Do you want to play as X or O? ")
#     if choose == "X":
#         player1 = "X"
#         player2 = "O"
#     else:
#         player1 = "X"
#         player2 = "O"
# else:
#     print("No problem! Come again when you feel like playing")
#
# # Function for finding the tile in the board and replacing with that players X or O
# # for p1def finding_tile_p1(position):
# def finding_tile_p1(position):
#     if position > 0 and position < 4:
#         for a in range(0,3):
#             if board1[a] == position:
#                 board1[a] = str(board1)
#                 board1 = player1
#     elif position > 3 and position < 7:
#         for b in range(0,3):
#             if board2[b] == position:
#                 board2[b] = str(board2)
#                 board2 = player1
#     else:
#         for c in range(0,3):
#             if board3[c] == position:
#                 board3[c] = str(board3)
#                 board3 = player1
#
# #for p2
# def finding_tile_p2(position):
#     if position > 0 and position < 4:
#         for a in range(0,3):
#             if board1[a] == position:
#                 board1[a] = str(board1)
#                 board1 = player2
#     elif position > 3 and position < 7:
#         for b in range(0,3):
#             if board2[b] == position:
#                 board2[b] = str(board2)
#                 board2 = player2
#     else:
#         for c in range(0,3):
#             if board3[c] == position:
#                 board3[c] = str(board3)
#                 board3 = player2
#
# # starting of the game
#
# if flag == "yes":
#
#     print("In order to play use your keyboard and type the number you want as seen below:")
#     print_the_board()
#
# # Make a loop where each time it asks p1 and p2 where they want to move
#     for turns in range(1,5):
#         turns = print("player 1 chose your position: ")
#         finding_tile_p1(turns)
#         print_the_board()
#         turns = print("player 2 chose your position: ")
#         finding_tile_p2()
#         print_the_board()
#
# #
# #SECOND TRY
# #
#
#
# # function which defines and displays the board
# def display_board(board):
#     print('   |   |')
#     print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
#     print('   |   |')
#     print('-----------')
#     print('   |   |')
#     print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
#     print('   |   |')
#     print('-----------')
#     print('   |   |')
#     print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
#     print('   |   |')
#
#
# game_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
#
# # Do you want to play the game
#
# flag = input("Do you want to play Tic Tac Toe? (yes or no) ")
#
# # choose x or o
# if flag == "yes":
#     choose = input("Player 1: Do you want to play as X or O? ")
#     if choose == "X":
#         player1 = "X"
#         player2 = "O"
#     else:
#         player1 = "O"
#         player2 = "X"
#     print("Hence Player 2 play as " + player2)
# else:
#     print("No problem! Come again when you feel like playing")
#
#
# # Function in order to put the move and replace it on the game board one for player1 and one for player 2
# def placing_marker(move, player):
#     for x in range(0, 9):
#         if game_board[x] == move:
#             game_board[x] = player
#
#
# # For checking if the game has been won or drawn
# def win(board, player):
#     result = 0
#     for q in range(0, 7, 3):
#         if board[q] == player and board[q + 1] == player and board[q + 2] == player:
#             result += 1
#
#     for a in range(0, 3):
#         if board[a] == player and board[a + 3] == player and board[a + 3] == player:
#             result += 1
#
#     for c in range(0, 3, 2):
#         if board[c] == player and board[c + 2] == player and board[c + 4] == player:
#             result += 1
#
#     return result
#
#
# def win_draw(result, board, player):
#     if result > 0:
#         print("Congratulations " + player + " you have won!")
#     elif board[0] == player1 and board[1] == player1 and board[2] == player1 and board[3] == player1 and board[
#         4] == player1 and board[5] == player1 and board[6] == player1 and board[7] == player1 and board[8] == player1 or \
#             board[0] == player2 and board[1] == player2 and board[2] == player2 and board[3] == player2 and board[
#         4] == player2 and board[5] == player2 and board[6] == player2 and board[7] == player2 and board[8] == player2:
#         print("The game is a draw")
#     else:
#         pass
#
#
# # how to play
# if flag == "yes":
#     print(
#         "In order to play use your keyboard and enter the position you wanna place your marker on. The positions are as below: ")
#     display_board(game_board)
#     print("Now lets begin!")
#
#     # Playing the game and testing each time weather or not the game is won or drawn
#
#     for turns in range(1, 6):
#         p1_move = input("Player 1 its your turn type the position you wanna place your {} ".format(player1))
#         placing_marker(p1_move, player1)
#         if turns >= 3:
#             win_draw(game_board, player1)
#
#         display_board(game_board)
#
#         p2_move = input(f"Player 2 its your turn, type the position you wanna place your {player2} ")
#         placing_marker(p2_move, player2)
#         if turns >= 3:
#             win_draw(game_board, player2)
#         display_board(game_board)



# # function which defines and displays the board
# def display_board(board):
#     print('   |   |')
#     print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
#     print('   |   |')
#     print('-----------')
#     print('   |   |')
#     print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
#     print('   |   |')
#     print('-----------')
#     print('   |   |')
#     print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
#     print('   |   |')
#
#
# game_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
#
# # Do you want to play the game
#
# flag = input("Do you want to play Tic Tac Toe? (yes or no) ")
#
# # choose x or o
# if flag == "yes":
#     choose = input("Player 1: Do you want to play as X or O? ")
#     if choose == "X":
#         player1 = "X"
#         player2 = "O"
#     else:
#         player1 = "O"
#         player2 = "X"
#     print("Hence Player 2 play as " + player2)
# else:
#     print("No problem! Come again when you feel like playing")
#
#
# # Function in order to put the move and replace it on the game board one for player1 and one for player 2
# def placing_marker(move, player):
#     for x in range(0, 9):
#         if game_board[x] == move:
#             game_board[x] = player
#
#
# # For checking if the game has been won or drawn
# def win(board, player):
#     result = 0
#     for q in range(0, 7, 3):
#         if board[q] == player and board[q + 1] == player and board[q + 2] == player:
#             result += 1
#
#     for a in range(0, 3):
#         if board[a] == player and board[a + 3] == player and board[a + 3] == player:
#             result += 1
#
#     for c in range(0, 3, 2):
#         if board[c] == player and board[c + 2] == player and board[c + 4] == player:
#             result += 1
#
#     return result > 0
#
# # to see if space is empty
# def empty_tile(board, position):
#     return board[position] == " "
#
# # to see if the full board is occupied as then it is a tie
#
# def tie_check(board):
#     for i in range(1,10):
#         if empty_tile(board, i):
#             return False
#     return True
#
# # def win_draw(result, board, player):
# # if result > 0:
# #     print("Congratulations " + player + " you have won!")
# # elif board[0] == player1 and board[1] == player1 and board[2] == player1 and board[3] == player1 and board[
# #     4] == player1 and board[5] == player1 and board[6] == player1 and board[7] == player1 and board[8] == player1 or \
# #         board[0] == player2 and board[1] == player2 and board[2] == player2 and board[3] == player2 and board[
# #     4] == player2 and board[5] == player2 and board[6] == player2 and board[7] == player2 and board[8] == player2:
# #     print("The game is a draw")
# # else:
# #     pass
#
#
# # how to play
# if flag == "yes":
#     print(
#         "In order to play use your keyboard and enter the position you wanna place your marker on. The positions are as below: ")
#     display_board(game_board)
#     print("Now lets begin!")
#
#     # Playing the game and testing each time weather or not the game is won or drawn
#
#     while True:
#         p1_move = input("Player 1 its your turn type the position you wanna place your {} ".format(player1))
#         placing_marker(p1_move, player1)
#         if turns >= 3:
#             win_draw(game_board, player1)
#
#         display_board(game_board)
#
#         p2_move = input(f"Player 2 its your turn, type the position you wanna place your {player2} ")
#         placing_marker(p2_move, player2)
#         if turns >= 3:
#             win_draw(game_board, player2)
#         display_board(game_board)
#
# # the game itself
#
# while True:
#     print("Player 1 its your turn:")
#
#     if flag.lower()[0] == "y":
#
#         display_board(game_board)
#         place_marker(game_board, player1_marker, position)
#
#         if win_check(game_board, player1_marker):
#             display_board(game_board)
#             print('Congratulations! You have won the game!')
#             game_on = False
#         else:
#             if tie_check(game_board):
#                 display_board(game_board)
#                 print('The game is a draw!')
#                 break
#             else:
#                 turn = 'Player 2'
#
#     else:
#         # Player2's turn.
#
#         display_board(game_board)
#         position = player_choice(game_board)
#         place_marker(game_board, player2_marker, position)
#
#         if win_check(game_board, player2_marker):
#             display_board(game_board)
#             print('Player 2 has won!')
#             game_on = False
#         else:
#             if tie_check(game_board):
#                 display_board(game_board)
#                 print('The game is a draw!')
#                 break
#             else:
#                 turn = 'Player 1'
#
# if not replay():
#     break

