#Tictactoe
import random
gamestart = None
def display_board(board):
    '''This displays the update board after each move'''
    print('\n'*100)
    print('   |   |')
    print(' ' + board[7] +' | '  + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | '  + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | '  + board[2] + ' | ' + board[3])
    print('   |   |')
def wanttoplay():
    '''This asks the player if they want to play'''
    gamestart = False 
    acceptrange = ['Y','N']
    pdecided = False
    while pdecided is False:
        playerdec = input("Would you like to play Tic Tac toe? Y or N? ").capitalize()
        print(playerdec)
        if playerdec not in acceptrange:
            print("Please answer Y or N! Y to play, N to leave!")
            playerdec = ""
        if playerdec == 'Y':
            print('Welcome to hell.. I mean tictactoe')
            gamestart = True
            pdecided = True
        if playerdec == 'N':
            pdecided = True
        else:
            pass
    return gamestart
def full_board_check(board):
    '''This checks to make sure the board has available spots'''
    count = 0
    for letter in board:
        if letter in ('X','O'):
            count += 1
        if count == 9:
            print("This is a tie!")
            return True
    return False
def replay2():
    '''This allows the player to play again, or stop playing'''
    goagain = input('Do you want to play again? Y or N? ')
    if goagain.capitalize() == 'Y':
        gameishere2()
    else:
        print("Thanks for playing Tictactoe!")
        gamestart = False
    return gamestart
def turndecider():
    '''This starts the game on a random players piece'''
    p_turn = False
    result = random.randint(1,2)
    if result == 2:
        p_turn = True
    return p_turn
def p_plays(board,p_turn,piece):#pylint: disable E1120
    '''this defines a players play and checks to make sure it is valid'''
    pchoicerange = range(1,10)
    pchoice = input("Please " + piece + " make your move! ")
    pchoicecheck = int(pchoice)
    if pchoicecheck not in pchoicerange:
        print("Too high 1-9 please!")
        p_plays(p_turn,board)
        return
    else:
        if (board[pchoicecheck] == 'O' or board[pchoicecheck] == 'X'):
            print("That space is taken")
            p_plays(board,p_turn,piece)
            return
        else:
            board[pchoicecheck]= piece
            display_board(board)
            p_turn = not p_turn
            return p_turn
def player(p_turn):
    '''This defines which player is playing'''
    if p_turn is True:
        piece = 'X'
    elif p_turn is False:
        piece = 'O'
    return piece
def wincondition2(board,piece):
    '''This picks a winner '''
    return ((board[1]==piece and board[2]==piece and board[3]==piece) or
        (board[4]==piece and board[5]==piece and board[6]==piece) or
        (board[7]==piece and board[8]==piece and board[9]==piece) or
        (board[7]==piece and board[4]==piece and board[1]==piece) or
        (board[8]==piece and board[5]==piece and board[2]==piece) or
        (board[9]==piece and board[6]==piece and board[3]==piece) or
        (board[7]==piece and board[5]==piece and board[3]==piece) or
        (board[9]==piece and board[5]==piece and board[1]==piece))
def gameishere2():
    ''' This starts the game '''
    doyouplay = wanttoplay()
    board = ['#','1','2','3','4','5','6','7','8','9']
    p_turn = turndecider()
    while doyouplay is True:
        display_board(board)
        player(p_turn)
        piece = player(p_turn)
        p_turn = p_plays(board,p_turn,piece)
        if wincondition2(board,piece) is True:
            print('You have won the game')
            display_board(board)
            if p_turn is True:
                print(piece+ "wins")
            else:
                print(piece+ "wins!")
            doyouplay = replay2()
        elif full_board_check(board) is True:
            print("Board is full!")
            doyouplay = replay2()

if __name__ == "__main__":
    gameishere2()
