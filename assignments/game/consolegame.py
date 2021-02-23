import deck, blackjack, blackjack_dealer, blackjack_player


while True:
    name = input('what is your name?\n')
    player = blackjack_player.BlackjackPlayer(name)
    dealer = blackjack_dealer.BlackjackDealer()
    gamedeck = deck.Deck()
    gamedeck.build()
    game = blackjack.Blackjack(gamedeck, (player, dealer))
    gamedeck.shuffle()
    gamedeck.shuffle()

    game.deal(gamedeck)
    

    while True:
        decision = input('hit or stand?')
        if decision == 'hit':
            player.hit(gamedeck)
            if player.total > 21:
                print('dealer wins')
                break
            print('HAND TOTAL: ', player.total)
            player.showHand()
            continue
        elif decision == 'stand':
            dealer.turn(gamedeck)
            break
        else:
            ValueError
    
    if dealer.total > player.total and dealer.total <= 21:
        print('Dealer wins')
        dealer.showHand()
    else:
        print('{} wins!!!'.format(player.name))

