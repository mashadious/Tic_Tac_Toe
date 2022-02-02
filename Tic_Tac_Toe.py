#---- Global Variables ----

#Game Board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#Game is still going
game_still_going = True

#Who won?
winner = None

#Who's turn it is
current_player = "X"

#Display the Board
def display_board():
    print(board[0]+ "|" + board[1]+ "|"+ board[2])
    print(board[3]+ "|" + board[4]+ "|"+ board[5])
    print(board[6]+ "|" + board[7]+ "|"+ board[8])

#Handles a single turn of one of the 2 players
def handle_turn(current_player):

    print (current_player, "'s turn. ")

    position = input("Choose a position from 1 to 9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position=input("Please enter a number between 1 and 9: ")

        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there, choose another position. ")
    board[position]= current_player
    display_board()

#Check if the game is over
def check_game_over():

    check_for_winner()
    check_tie()
#Check if the game is a tie
def check_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def check_for_winner():

    global game_still_going
    global winner
    #Check Columns
    columns_winner=check__columns()
    #Check Rows
    rows_winner=check__rows()
    #Check Diagonals
    diagnols_winner=check__diagonals()

    #Get the Winner
    if rows_winner:
        #there was a win
        winner = rows_winner
    elif columns_winner:
        #there was a win
        winner = columns_winner
    elif diagnols_winner:
        #there was a win
        winner = diagnols_winner
    else:
        #there was no win
        winner = None
    return

def check__rows():
    #
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    row_1 = board [0] == board [1] == board [2] != "-"
    row_2 = board [3] == board [4] == board [5] != "-"
    row_3 = board [6] == board [7] == board [8] != "-"
    #If any row does have a match, flag that there is a win:
    if row_1 or row_2 or row_3:
        game_still_going = False
        # Return the winner (X or O)
        if row_1:
            return board[0]
        elif row_2:
            return board[3]
        elif row_3:
            return board[6]
    return

def check__columns():
    # Check if any of the rows have all the same value (and is not empty)
    global game_still_going
    column_1 = board [0] == board [3] == board [6] != "-"
    column_2 = board [1] == board [4] == board [7] != "-"
    column_3 = board [2] == board [5] == board [8] != "-"
    #If any row does have a match, flag that there is a win:
    if column_1 or column_2 or column_3:
        game_still_going = False
        # Return the winner (X or O)
        if column_1:
            return board[0]
        elif column_2:
            return board[1]
        elif column_3:
            return board[2]
    return

def check__diagonals():
    # Check if any of the rows have all the same value (and is not empty)
    diagonal_1 = board [0] == board [4] == board [8] != "-"
    diagonal_2 = board [6] == board [4] == board [2] != "-"
    global game_still_going
    #If any row does have a match, flag that there is a win:
    if diagonal_1 or diagonal_2 :
        game_still_going = False
        # Return the winner (X or O)
        if diagonal_1:
            return board[0]
        elif diagonal_2:
            return board[6]

    return

#Flip to the other player
def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

#Play a game of Tic Tac Toe
def play_game():

    #Display initial board
    display_board()

#While the game is still going
    while game_still_going:

    #Handles a single turn of one of the 2 players
        handle_turn(current_player)

        #Check if The game is over
        check_game_over()

        #Flip to the other player
        flip_player()

    check_for_winner()
    if winner == "X" or winner =="O":
        print(winner,"won.")
    elif winner == None:
        print("Tie.")


play_game()
