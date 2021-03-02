import game, blackjack_player, deck, card

class Blackjack(game.Game):
    '''
    arguements:
        player list

    attributes:
        player_list
        deck
        dealer
        winner
    '''
    def __init__(self, *player_list):
        self.player_list = [*player_list]
        self.deck = deck.Deck()
        self.dealer = blackjack_player.BlackjackDealer()
        self.winner = self.dealer

# DECK RELATED FUNCTIONS

    def readyDeck(self):
        self.deck.cards = []
        self.deck.build()
        self.deck.shuffle()

    def draw(self, player):
        card = self.deck.draw()
        player.hand.append(card)
        self.addCardToTotal(card, player)

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
            self.playerTurn(player)
        self.dealerTurn()

    def determineWinner(self):
        for player in self.player_list:
            if player.total <= 21:
                if player.total < self.winner.total:
                    self.winner = player
        print(self.winner.name, ' wins!!!')

    def playGame(self):
        self.readyDeck()
        self.deal()
        self.round()
        self.determineWinner()

# DEALER TURN FUNCTIONS

    def dealerTurn(self):
        if self.dealer.total < 17:
            self.hit(self.dealer)
            self.dealer.showHand()
            self.dealerPlay()

    def dealerPlay(self):
        for player in self.player_list:
            if player.isBusted == False:
                self.dealerTurn()
        else:
            self.determineWinner()

# PLAYER TURN FUNCTIONS

    def playerTurn(self, player):
        decision = input('Hit or Stand?\n')
        if decision.lower() == 'hit':
            self.hit(player)
            self.playerTurn(player)
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
        # draw calls 'self.addCardToTotal'
    
# HIT/ACE/BUST CHECKS

    def addCardToTotal(self, card, player):
        if card.value == 'Ace':
            self.aceHit(card, player)
        elif card.value == 'Jack' or card.value == 'Queen' or card.value == 'King':
            player.total += 10
        else:
            player.total += card.value
        self.finalBustCheck(player)

    def aceHit(self, card, player):
        if player.total + 11 > 21:
            player.total += 1 
            card.status = True
        else:
            player.total += 11

    def bustedAce(self, player):
        for card in player.hand:
            if card.value == 'Ace' and card.status == False:
                player.total -= 10
                card.status = True  

    def bustAceCheck(self, player):
        if player.total > 21:
            self.bustedAce(player)
    
    def isPlayerBusted(self):
        for player in self.player_list:
            if player.total > 21:
                player.isBusted = True

    def finalBustCheck(self, player):
        self.bustAceCheck(player)
        self.isPlayerBusted()
