import blackjack, blackjack_dealer, blackjack_player

josh = blackjack_player.BlackjackPlayer('Josh')
game = blackjack.Blackjack(josh)
game.readyDeck()
game.deal()
game.dealerTurn()

