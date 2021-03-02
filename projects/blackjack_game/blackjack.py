from game import *
from blackjack_player import *
from deck import *


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
        determine_winner - evaluate scores,
        play_game - ready_deck, deal, round, determine_winner,

        dealer_turn - dealer hits,
        dealer_play - dealer decides what to do,

        player_turn - gets input from player decision,
        hit - adds a card to players hand and implements logic,

        add_card_to_total - the following methods need to be simplified
        ace_hit
        busted_ace
        busted_ace_check
        are_players_busted
        are_players_busted
        finalBustCheck  
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

    def determine_winner(self):
        for player in self.player_list:
            if player.total <= 21:
                if player.total < self.winner.total:
                    self.winner = player
        print(self.winner.name, ' wins!!!')

    def play_game(self):
        self.ready_deck()
        self.deal()
        self.round()
        self.determine_winner()

# DEALER TURN FUNCTIONS

    def dealer_turn(self):
        if self.dealer.total < 17:
            self.hit(self.dealer)
            self.dealer.showHand()
            self.dealer_play()

    def dealer_play(self):
        for player in self.player_list:
            if player.isBusted == False:
                self.dealer_turn()
            else:
                self.determine_winner()

# PLAYER TURN FUNCTIONS

    def player_turn(self, player):
        decision = input('Hit or Stand?\n')
        if decision.lower() == 'hit':
            self.hit(player)
            self.player_turn(player)
            player.showHand()
        elif decision.lower() == 'stand':
            pass
        elif player.total > 21:
            pass
        else:
            ValueError

    def hit(self, player):
        self.draw(player)
        player.showHand()
        # draw calls 'self.add_card_to_total'
    
# HIT/ACE/BUST CHECKS

    def add_card_to_total(self, card, player):
        if card.value == 'Ace':
            self.ace_hit(card, player)
        elif card.value == 'Jack' or card.value == 'Queen' or card.value == 'King':
            player.total += 10
        else:
            player.total += card.value
        self.finalBustCheck(player)

    def ace_hit(self, card, player):
        if player.total + 11 > 21:
            player.total += 1 
            card.status = True
        else:
            player.total += 11

    def busted_ace(self, player):
        for card in player.hand:
            if card.value == 'Ace' and card.status == False:
                player.total -= 10
                card.is_used = True  

    def busted_ace_check(self, player):
        if player.total > 21:
            self.busted_ace(player)
    
    def are_players_busted(self):
        for player in self.player_list:
            if player.total > 21:
                player.isBusted = True

    def finalBustCheck(self, player):
        self.busted_ace_check(player)
        self.are_players_busted()

poop = Blackjack()