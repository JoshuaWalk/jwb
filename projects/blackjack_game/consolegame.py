from blackjack import *


name = input('Enter your name to play blackjack:\n')
player = Player(name)
game = Blackjack(player)
game.play_game()

