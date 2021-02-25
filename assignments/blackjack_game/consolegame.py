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
    player.showHand()
    print(player.hand)
    

    while True:
        decision = input('hit or stand?\n')
        if decision == 'hit':
            player.hit(gamedeck)
            if player.total > 21:
                print('{} busts!!\n'.format(player.name))
                break
            print('HAND TOTAL: ', player.total)
            player.showHand()
            continue
        elif decision == 'stand':
            dealer.turn(gamedeck)
            break
        else:
            ValueError
    
    print(game.determineWinner(), ' wins!!!\n')

