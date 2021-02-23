import deck, blackjack, blackjack_dealer, blackjack_player

#initialize game classes

deck = deck.Deck()
player = blackjack_player.BlackjackPlayer('Josh')
dealer = blackjack_dealer.BlackjackDealer()
game = blackjack.Blackjack(deck, (player, dealer))

#build/shuffle deck

deck.build()
deck.shuffle()
deck.shuffle()

#start game

