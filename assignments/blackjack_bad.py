import random
while True:
    suite = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 'A']
    deck = suite * 4

    player = []
    player_total = 0

    dealer = []
    dealer_total = 0

# PLAYER FUNCTIONS

    def check_player_ace():
        for x in player:
            if x == 'A':
                player.remove('A')
                ace = input('You got an Ace! Would you like it to count as 1 or 11\n')
                print('ACE: \n', ace)
                if ace == '1':
                    player.append(1)
                elif ace == '11':
                    player.append(11)

    def check_player_total():
        global player_total
        local_total = 0
        for x in player:
            local_total += x
        if player_total > 21:
                print('you busted!')
        elif player_total == 21:
                print('you got blackjack!')
        player_total = local_total
        local_total = 0
        print("CHECKPLAYERTOTAL\nPLAYER TOTAL:\n", player_total)
                

    def deal_player():
        player.append(random.choice(deck))
        print('Your Hand:\n',player)
        check_player_ace()
        check_player_total()
    

# DEALER FUNCTIONS

    def check_dealer_total():
        global dealer_total
        local_total = 0
        for x in dealer:
            if x == 'A':
                print('found an A\n')
                continue                
            else:
                local_total += x
                print("DEALER TOTAL:\n", local_total)
        for x in dealer:
            if x == 'A':
                print('found an a again!\n')
                if local_total + 11 > 21:
                    dealer.append(1)
                    local_total += 1
                    continue
                else:
                    dealer.append(11)
                    local_total += 11
                    continue
        if 'A' in dealer:
            dealer.remove('A')
        if dealer_total > 21:
            print('Dealer busts!! YOU WIN!!!')
        dealer_total = local_total    
        local_total = 0

    def check_win():
        if player_total > dealer_total and player_total <= 21:
            print('player wins!')
        elif dealer_total > player_total and dealer_total <= 21:
            print('dealer wins!')
        elif player_total == dealer_total:
            print('It is a tie!')


    def deal_dealer():
        dealer.append(random.choice(deck))
        check_dealer_total()
                               
    def deal_start():
        deal_player()
        deal_dealer()
        deal_player()
        deal_dealer()
        print("player hand:" , player, "\n", "dealer hand:", dealer)
        check_player_ace()
    
    def play_game():
        deal_start()
        while True:
            choice = input('Hit or Stand?\n')
            if choice == 'hit':
                deal_player()
            elif choice == 'stand':
                deal_dealer()
            else:
                continue



    play = input('Would you like to play blackjack? y/n\n')            
    if play == 'y':
        play_game()
    else: 
        break


# deal function
    # give player 1 card, dealer 1 face down card, then both 1 card face up

# players turn
    # check for blackjack
    # ask player if they want to get another card or stop
    # check for busts
    # loop

# dealers turn
    # reveal hidden card
    # if hand < 17 dealer hits
    # check for bust
    # loop

# evaluate bet
    # if dealer busts player wins
    # if no busts, higher points win