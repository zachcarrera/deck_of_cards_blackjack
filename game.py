import random
import os
from classes.deck import Deck

# clear = lambda: os.system('clear')

def clear():
    os.system('clear')


# ------- Blackjack ---------

# Deck
# Player hand
# Dealer hand
# hit function

# stand
# buts == > 21

# value for hands
#  ace is 1 or 11
# dealer cant hit if value is over 16

# create random for dealer and player



# ASCII art for logo

logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""



# while the user inputs "y" to the terminal:
while input("Do you want to play a game of Blackjack? Type 'y' to play, 'n' to exit: ") == 'y':


    # clear the console and print the logo
    clear()
    print(logo)

    # initialize the deck of cards
    bicycle = Deck()


    # make player and dealer hands
    player_hand = []
    dealer_hand = []

    # start player and dealer at 0 points
    player_value = 0
    dealer_value = 0


    # deal two random cards to the player and dealer
    for i in range(4):
        x = random.choice(bicycle.cards)
        if i % 2 == 0:
            player_hand.append(x)
        else:
            dealer_hand.append(x)

        # remove card "x" from deck
        bicycle.cards.remove(x)


    # print the player info
    print("Player")
    for card in player_hand:
        card.card_info()
        player_value += card.point_val

    print("Player points:", player_value)

    print("---------------")

    # print the dealer info
    print("Dealer")
    for card in dealer_hand:
        card.card_info()
        dealer_value += card.point_val

    print("Dealer points:", dealer_value)

    print("---------------")

    # deal two more cards if allowed
    for i in range(2):
        x = random.choice(bicycle.cards)
        if i % 2 == 0 and player_value < 17:
            player_hand.append(x)
            print("Player hits")
            x.card_info()
            player_value += x.point_val
        elif dealer_value < 17:
            dealer_hand.append(x)
            print("Dealer hits")
            x.card_info()
            dealer_value += x.point_val

        # remove card "x" from deck
        bicycle.cards.remove(x)

    print("---------------")


    print("Player points:", player_value)
    print("Dealer points:", dealer_value)


    # logic to determine winner
    if player_value > 21 and dealer_value > 21:
        print(" You busted. You lose 😭")
    elif dealer_value == player_value:
        print("Draw 🤝")
    elif dealer_value == 21: 
        print("Dealer has a Blackjack. You lost 😭")
    elif player_value == 21:
        print("BLACKJACK. You win  🥇")
    elif player_value > 21:
        print("You busted! Dealer wins 😤")
    elif dealer_value > 21:
        print("Dealers busts. You win 🤩")
    elif player_value > dealer_value:
        print("You win. 🥇")
    else:
        print("You lose. 😭")
