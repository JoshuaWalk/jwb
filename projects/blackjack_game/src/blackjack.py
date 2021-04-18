from src.game import *
from src.blackjack_player import *
from src.deck import *


class Blackjack(Game):
    '''
    arguements:
        player_list

    attributes:
        player_list,
        deck,
        dealer,
        winner,

    methods:
        ready_deck - builds a new deck and shuffles cards,
        draw - takes a card from deck,

        deal - deals 2 cards to every player,
        round - every player takes a turn,
        reset_game - refreshes everyones totals + hands + deck + starts new deal,
        is_winning - determines if a player is leading,
        display_winner - self explanitory

        dealer_turn - dealer hits,
        dealer_play - dealer decides what to do,

        player_turn - gets input from player decision,
        hit - adds a card to players hand and implements logic,

        add_card_to_total,
        ace_hit,
        busted_ace,
        is_player_busted,
 
    '''

    def __init__(self, *player_list):
        self.player_list = [*player_list]
        self.deck = Deck()
        self.dealer = BlackjackDealer()
        self.winner = self.dealer

# DECK RELATED FUNCTIONS

    def ready_deck(self):
        self.deck.cards = []
        self.deck.build()
        self.deck.shuffle()

    def draw(self, player):
        card = self.deck.draw()
        player.hand.append(card)
        self.add_card_to_total(card, player)

# GAME MANAGEMENT FUNCTIONS

    def deal(self):
        for player in self.player_list:
            self.draw(player)
            self.draw(player)
            player.showHand()
        self.draw(self.dealer)
        self.draw(self.dealer)
        self.dealer.showHand()

    def round(self):
        for player in self.player_list:
            self.player_turn(player)
        self.dealer_turn()

    def is_winning(self, player):
        if player.total <= 21 and player.total > self.winner.total:
            self.winner = player
    
    def display_winner(self):
        print(f'\n{self.winner.name} wins!')
        self.winner.showHand()

    def reset_game(self):
        self.winner = self.dealer
        self.dealer.restart()
        for player in self.player_list:
            player.restart()
        self.ready_deck()
        self.deal()
        self.round()
        self.display_winner()

# DEALER TURN FUNCTIONS

    def dealer_turn(self):
        if self.dealer.total < 17 and self.dealer.total < self.winner.total:
            self.hit(self.dealer)
            self.dealer.showHand()
            self.dealer_play()

    def dealer_play(self):
        for player in self.player_list:
            if player.is_busted == False:
                self.dealer_turn()
            else:
                self.is_winning(self.dealer)

# PLAYER TURN FUNCTIONS

    def player_turn(self, player):
        if player.is_busted == True:
            pass
        else:
            decision = input('Hit or Stand?\n')
            if decision.lower() == 'hit':
                self.hit(player)
                self.player_turn(player)
                player.showHand()
            elif decision.lower() == 'stand':
                self.is_winning(player)
            else:
                ValueError

    def hit(self, player):
        self.draw(player)
        player.showHand()
        # draw calls 'self.add_card_to_total'
    
# HIT/ACE/BUST CHECKS

    #player hits
    def add_card_to_total(self, card, player):
        if card.value == 'Ace':
            self.ace_hit(card, player)
        elif card.value == 'Jack' or card.value == 'Queen' or card.value == 'King':
            player.total += 10
        else:
            player.total += card.value
        self.is_player_busted(player)

    #if a player pulls an ace
    def ace_hit(self, card, player):
        if player.total + 11 > 21:
            player.total += 1 
            card.is_used = True
        else:
            player.total += 11

    #if a player busts

    def busted_ace(self, player):
        for card in player.hand:
            if card.value == 'Ace' and card.is_used == False:
                if player.total <= 21: break
                player.total -= 10
                card.is_used = True
                
    def is_player_busted(self, player):
            self.busted_ace(player)
            if player.total > 21:
                player.is_busted = True


    

    

    
    
    

    
