#mainconfig
#This will be the main configuration for my game hub!
#Thats about as far as I know to go will be learning!
from GameCenter.game_logics import setup
pickedgame = False
while pickedgame is False:
    try:
        p_pick = input("Please pick a game: Blackjack or Tictactoe!").lower()
        if p_pick[0] == "b":
            setup.main_classes.blackjack()
            pickedgame = True #pylint DISABLE C0103
        elif p_pick[0] == "t":
            setup.tictactoe.gameishere2()
            pickedgame = True
    except:
        print("Sorry, please enter B for blackjack or T for tictactoe!")
        pickedgame = False

if __name__ == "__main__":
    pass
