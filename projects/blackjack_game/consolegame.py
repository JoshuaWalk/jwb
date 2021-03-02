import blackjack, blackjack_player

name = input('Enter your name to play blackjack:\n')
player = blackjack_player.Player(name)
game = blackjack.Blackjack(player)
game.playGame()

