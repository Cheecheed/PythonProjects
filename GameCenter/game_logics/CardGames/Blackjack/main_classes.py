#Card, Deck, Player Class.
#values to create deck from
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


class Card:
    #allows creation of individual card objects with values derived from the values dictionairy.
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        #provides a string representation of cards
        #Consider this to be where you can add a visual representation maybe?
        return self.rank + " of " + self.suit


class Deck:
    #allows the creation/interactions between decks.
    def __init__(self):

        self.all_cards = []
        #this for loop creates the deck of 52 unique cards using the suits/ranks lists
        for suit in suits:
            for rank in ranks:
                # create card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        #this shuffles the deck
        random.shuffle(self.all_cards)

    def deal_one(self):
        #this is how you remove a card from the deck
        return self.all_cards.pop(0)


class Player:
    #this is the individual user information. Consider adding database manipulation to the core mechanics in the future.
    #Consider adding a class for chips, so each can have a catagorized value#

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.all_cards = []

    def new_hand(self):
        #this defines an empty hand(starting a new round)
        self.all_cards = []

    def add_cards(self, new_cards):
        #this adds cards to players hand that have been dealt from the Deck class using deal_one()
        #example is self.all_cards.extend(Deck.deal_one()) <-- this adds a single card from the deck, while also removing
        #the card from the unique collection of cards inside the "deck"
        if type(new_cards) is type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def betting(self):
        #this is how a player places bets. Using this logic, it updates the unique players balance until the end of game
        #consider creating this inside Chips class, as it would be a direct interaction with those, and have Chips class
        #tie into player balance in DB
        allin_dec = False
        betplaced = False  # bet starts off as 0, edited later
        while betplaced == False:
            while allin_dec == False:
                go_all_in = input(f'Would you like to go all in? You have {self.balance}: Y or N: ').upper()
                '''This allows the player to bet all of there current balance'''
                if go_all_in == 'Y':
                    bet = self.balance
                    betplaced = True
                    allin_dec = True
                    print(f'you are betting {bet}, you have {self.balance - bet} left')
                    return bet
                if go_all_in == 'N':
                    remark = random.randint(1, 5)
                    if remark == 1:
                        print(f"{self.name} is a chicken")
                        allin_dec = True
                    if remark == 2:
                        print("Coward")
                        allin_dec = True
                    if remark == 3:
                        print("Too scared to bet big???")
                        allin_dec = True
                    if remark == 4:
                        print(f"{self.name} is a scaredy Cat")
                        allin_dec = True
                    if remark == 5:
                        print(f"{self.name} is afraid of losing {self.balance}. What are you; poor?")
                        allin_dec = True

                elif go_all_in != 'Y' or 'N':
                    print("Sorry I didn't understand, please try again.")
                    allin_dec = False
            if go_all_in == "N":
                amount = 0
                while amount == 0:
                    try:
                        amount = int(input(f"{self.name} how much would you like to bet? You have {self.balance}: "))
                    except:
                        print("I didn't quite get that sorry")
            if amount > self.balance:
                print(f"You don't have that much? Why not go all in?")
                allin_dec = False
            else:
                self.balance > amount
                bet = amount
                print(f"You are betting {bet} and have {self.balance - bet} left.")
                betplaced = True
        return bet
def replay2():
    #instantiates a replay question, prompting the user to decide to play again or not!
    goagain = input('Do you want to play again? Y or N? ')
    try:
        if goagain.capitalize() == 'Y':
            blackjack()
        else:
            print("Thanks for playing!")
    except:
        print("Sorry, I didnt understand, please try again.")
### GAME LOGIC BELOW! ###
def blackjack():
    game_over = False
    game_on = True
    hand = False
    tplayer = Player(input("Oh, you're finally awake. Welcome to blackjack! Who are you?: "), 500)
    dealer = Player("Dealer", 1)
    print("Welcome to blackjack.")
    print("Your goal is to beat the dealer! You can place bets before we deal each hand.")
    print("If you win your winnings are double your bet!")
    print("If you lose, you lose your bet. Duh.")
    print("Get a hand total higher than the dealer to win, but be careful! If you go over 21 you lose!")
    print("Getting an Ace and 10, Jack, Queen, or King, results in an automatic win for that hand!")
    print("Goodluck out there!")
    new_deck = Deck()
    new_deck.shuffle()
    # no cards = no value
    pl_hand = 0  # player
    de_hand = 0  # dealer
    bet = 0
    while game_on == True:
        if tplayer.balance >= 10000:
            print("You ran us out of money! I guess that means you win? Maybe seek therapy.")
            game_over = True
            game_on = False
        if tplayer.balance <= 0:
            print("You've run out of money! You lose! Come back when you aren't so poor!")
            game_over = True
            game_on = False
        else:
            is_round_done = False
        while is_round_done == False:
            if len(new_deck.all_cards) <= 12:
                new_deck = Deck()
                new_deck.shuffle()
            if tplayer.balance <= 0:
                print("You've run out of money! You lose! Come back when you aren't so poor!")
                game_on = False
                game_over = True
                break
            hitdec = False
            tplayer.all_cards = []
            dealer.all_cards = []
            pl_hand = 0
            de_hand = 0
            bet = 0
            pwin = False
            dwin = False
            pbust = False
            dbust = False
            if len(new_deck.all_cards) == 0:
                # incase the game has gone on long enough to get through 52 cards. Resets deck
                new_deck = Deck()
                new_deck.shuffle()
            # Cant play if you got no money
            # place your bets
            bet = tplayer.betting()
            tplayer.balance = tplayer.balance - bet
            # This is where the intial hand is dealt.
            tplayer.add_cards(new_deck.deal_one())
            # hand math
            pl_hand += tplayer.all_cards[-1].value
            print(f'Player: {tplayer.all_cards[-1]}, {tplayer.all_cards[-1].value}:')
            dealer.add_cards(new_deck.deal_one())
            # dealerhandmath
            de_hand += dealer.all_cards[-1].value
            print(f'Dealer: {dealer.all_cards[-1]}, {dealer.all_cards[-1].value}')
            tplayer.add_cards(new_deck.deal_one())
            pl_hand += tplayer.all_cards[-1].value
            print(f'Player: {tplayer.all_cards[-1]}, {tplayer.all_cards[-1].value} ')
            dealer.add_cards(new_deck.deal_one())
            de_hand += dealer.all_cards[-1].value
            print("Dealer sets his second card face down.")
            # Start of blackjack check
            blackjack = False
            pblackjack = False
            dblackjack = False
            while blackjack == False:
                if tplayer.all_cards[0].value == 11 or tplayer.all_cards[-1].value == 11:
                    if tplayer.all_cards[0].value == 10 or tplayer.all_cards[-1].value == 10:

                        pblackjack = True
                    else:
                        pass
                if dealer.all_cards[0].value == 11 or dealer.all_cards[-1].value == 11:
                    if dealer.all_cards[0].value == 10 or dealer.all_cards[-1].value == 10:
                        dblackjack = True
                    else:
                        pass
                if pblackjack and dblackjack == True:
                    tplayer.balance = tplayer.balance + bet ** 100
                    print("Both have blackjack! I thought this was impossible. Enjoy the money.")
                    hitdec = None
                    is_round_done = True
                    blackjack = True
                if pblackjack is True:
                    tplayer.balance = tplayer.balance + bet * 3
                    print(f"{tplayer.name} has scored a blackjack and wins the hand!")
                    hitdec = None
                    is_round_done = True
                    blackjack = True

                if dblackjack is True:
                    tplayer.balance = tplayer.balance - bet
                    print(f"{dealer.name} has scored a blackjack and wins the hand!")
                    hitdec = None
                    is_round_done = True
                    blackjack = True
                else:
                    blackjack = True
            # splitting
            # Can split any two cards of same rank.
            # Can split up too twice (total 3 hands)
            # aces can't be resplit ~~~ ???? lol who knos
            # when split both hands bet = first bet
            # can double down split hands
            # maybe not *casino* worthy but basic.

            # End of blackjack check
            while hitdec == False:  # maybe some issues here well see
                if pl_hand > 21:
                    pbust = True
                    print(f"{tplayer.name} busts!")
                    hitdec = True
                if pl_hand == 21:
                    hitdec = True
                if pl_hand < 21:
                    dec_to_hit = input(f"Want to hit {tplayer.name}? Hand total: {pl_hand} Y or N: ").capitalize()
                    if dec_to_hit == "N":
                        hitdec = True
                    if dec_to_hit == "Y":
                        tplayer.add_cards(new_deck.deal_one())
                        # handmath(idk if this will work)
                        pl_hand += tplayer.all_cards[-1].value
                        print(f'{tplayer.all_cards[-1]}, {tplayer.all_cards[-1].value} Dealer total: {de_hand}')
            # if player busted, this sets the dealer to winner and skips dealer turn
            if pbust == True:
                pl_hand = 0
                hitdec = False
                pwin = False
                dwin = True
            while hitdec == True:
                if de_hand < 17:
                    dealer.add_cards(new_deck.deal_one())
                    de_hand += dealer.all_cards[-1].value
                    print(f'{dealer.all_cards[-1]}, {dealer.all_cards[-1].value}, dealer hand total: {de_hand}')
                    hitdec = True
                if de_hand > 21:
                    dbust = True
                    print("Dealer busts")
                    print(f'Dealer hand total: {de_hand}')
                    hitdec = False
                else:
                    hitdec = False
            # if dealer busted, his hand value gets reset so all checks leave pwin as True
            if dbust == True:
                de_hand = 0
            if pl_hand > de_hand:
                print(f"Player won:{pl_hand} vs. {de_hand}")
                pwin = True
                dwin = False
            elif pl_hand < de_hand:
                print(f'Dealer won {de_hand} vs. {pl_hand}')
                pwin = False
                dwin = True
            else:
                print("It was a tie!")
                pwin = False
                dwin = True
            if pwin == True:
                tplayer.balance = tplayer.balance + bet * 2
                pwin = False
            # bet is taken off balance after being placed, so if they lose balance remains the same.
            if dwin == True:
                tplayer.balance = tplayer.balance
                dwin = False
            if pwin or dwin == True:
                is_round_done = True
    if game_over is True:
        replay2()
if __name__ == "__main__":
    pass

