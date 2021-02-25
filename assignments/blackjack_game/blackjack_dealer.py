import blackjack_player 

class BlackjackDealer(blackjack_player.BlackjackPlayer):
    def __init__(self):
        blackjack_player.BlackjackPlayer.__init__(self, 'Dealer')
        self.total = 0

    def hiddenHit(self, deck):
        card = self.drawCard(deck)
        if card.value == 'Ace':
            self.aceHit()
        elif card.value == 'King' or card.value == 'Queen' or card.value == 'Jack':
            self.total += 10
        else:
            self.total += card.value
        self.didBust()  

    def turn(self, deck):
        if self.total < 17:
            self.hiddenHit(deck)
            self.turn(deck)
            self.showHand()
        else:
            pass