from src.blackjack import *


name = input('Enter your name to play blackjack:\n')
player = Player(name)
game = Blackjack(player)

while True:
    decision = input('Would you like to play Blackjack? y / n\n')
    if decision == 'y':
        game.reset_game()
        continue
    elif decision == 'n':
        break
    ValueError(print("please enter 'y' or 'n'"))
