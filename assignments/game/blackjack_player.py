import player 

class BlackjackPlayer(player.Player):
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.total = 0
        self.isBusted = False

    def turn(self, decision):
        if decision == 'hit':
            self.aceCheck()
            self.hit()
            self.turn()
        else:
            self.stand()

    def hit(self, deck):
        card = self.drawCard(deck)
        if card.value == 'Ace':
            self.aceHit()
        if card.value == 'King' or card.value == 'Queen' or card.value == 'Jack':
            self.total + 10
        else:
            self.total += card.value
        self.didBust()

    def stand(self):
        return self

    def aceHit(self):
        if self.total + 11 > 21:
            self.total + 1
        else:
            self.total + 11
        
    
    def aceCheck(self):
        for card in self.hand:
            if card.value == 'Ace' and card.status == False:
                self.total - 10
                card.status = True

    def didBust(self):
        if self.total > 21:
            self.aceCheck()
            if self.total > 21:
                self.isBusted = True