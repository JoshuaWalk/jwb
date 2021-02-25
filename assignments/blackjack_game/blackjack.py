import game, blackjack_player, blackjack_dealer, deck, card

class Blackjack(game.Game):
    def __init__(self, *args):
        self.players = [*args]
        self.deck = deck.Deck()
        self.dealer = blackjack_dealer.BlackjackDealer()
        self.winner = self.dealer

    def readyDeck(self):
        self.deck.cards = []
        self.deck.build()
        self.deck.shuffle()

    def draw(self):
        return self.deck.cards.pop()
    
    def hit(self, player):
        card = self.draw()
        player.hand.append(card)
        self.addCardToTotal(card.value, player)

    def deal(self):
        for player in self.players:
            self.hit(player)
            self.hit(player)
            player.showHand()
        self.hit(self.dealer)
        self.hit(self.dealer)
        self.dealer.showHand()

    def addCardToTotal(self, card, player):
        if card == 'Ace':
            self.aceHit(card, player)
        elif card == 'Jack' or card == 'Queen' or card == 'King':
            player.total += 10
        else:
            player.total += card

    def aceHit(self, card, player):
        if player.total + 11 > 21:
            player.total += 1 
            card.status = True
        else:
            player.total += 11
    
    def dealerTurn(self):
        if self.dealer.total < 17:
            self.hit(self.dealer)
            self.dealer.showHand()
            self.dealerTurn()

    def determineWinner(self):
        for player in self.players:
            if player.total <= 21:
                if player.total < self.winner.total:
                    self.winner = player

    def playerTurn(self, decision, deck):
        if decision == 'hit':
            self.hit(deck)
            self.playerTurn()
        elif decision == 'stand':
            self.stand()


josh = blackjack_player.BlackjackPlayer('Josh')
game = Blackjack(josh)
game.readyDeck()
game.deal()
game.dealerTurn()