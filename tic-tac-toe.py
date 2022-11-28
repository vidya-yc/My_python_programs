#1 -Create display board
from IPython.display import clear_output

def display(test_board):
    clear_output()
    print(test_board[7] + "|" +test_board[8] + "|" +test_board[9])
    print(test_board[4] + "|" +test_board[5] + "|" +test_board[6])
    print(test_board[1] + "|" +test_board[2] + "|" +test_board[3])
#2 - Take input from user if they want to be '0' or 'X'
def player_input():
    marker =""

    while not(marker == 'X' or marker == "O"):
        marker = input("Player 1: Do you want to be X or O : ").upper()

    if marker == 'X':
        return ('X' , 'O')
    else:
        return ('O' , 'X')
player1_marker ,player2_marker = player_input()
print(player1_marker)
print(player2_marker)
#3 -Fill the user value on board
def place_marker(board, marker, position):
    board[position] = marker
test_board = ["Z" , "A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I"]
display(test_board)
place_marker(test_board , "P" , 4)
display(test_board)
#4 - Winning goals
def win_check(board , mark):
    return( (board[7] == mark and board[8] == mark and board[9] == mark) or #across the top,
            (board[4] == mark and board[5] == mark and board[6] == mark) or   #across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  #across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or#down the left side
            (board[2] == mark and board[8] == mark and board[5] == mark) or#down the middle
            (board[3] == mark and board[6] == mark and board[9] == mark) or#down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or#2 diagonals
            (board[9] == mark and board[5] == mark and board[1] == mark)
          )
#5 - if space is empty
def space_check(board , position):
    return board[position] == " "
#6 - Decide whose turn is first
import random

def choose_first():
    if random.randint( 0 , 1 ) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
#7 - if board is already full
def full_board_check(board):
    for i in range( 1 , 10):
        if space_check(board , i):
            return False
        return True
#8 - Take the input from the user
def player_choice(board):
    position = 0
    while position not in [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ] or not space_check(board , position):
        position = int(input("Enter your position (1-9)"))

    return position
#9 - If user wants to play it again
def replay():
    return input("You want to play again (yes , no)").lower().startswith('y')
#10 - Compile all
print("WELCOME TO TIC-TAC-TOE!!!")

while True:
    theBoard = [' ']*10
    player1_marker ,player2_marker = player_input()
    turn = choose_first()
    print(turn + " Will go first ")

    play_game = input("Do you want to play it again(Yes/No)")

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':

            display(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard , player1_marker , position)

            if win_check(theBoard , player1_marker):
                display(theBoard)
                print("CONGRATULATIONS!! You have WON the game")
                game_on = False

            else:
                if full_board_check(theBoard):
                    display(theBoard)
                    print("The game is DRAW!!")
                    break
                else:
                    turn = "Player 2"


        else:
            display(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard , player1_marker , position)

            if win_check(theBoard , player1_marker):
                display(theBoard)
                print("CONGRATULATIONS!! You have WON the game")
                game_on = False

            else:
                if full_board_check(theBoard):
                    display(theBoard)
                    print("The game is DRAW!!")
                    break
                else:
                    turn = "Player 1"


    if not replay():
        break
