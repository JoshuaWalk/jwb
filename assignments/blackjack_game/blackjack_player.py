import player 

class BlackjackPlayer(player.Player):
    def __init__(self, name):
        player.Player.__init__(self, name)
        self.isBusted = False

    def hit(self, deck):
        card = self.drawCard(deck)
        if card.value == 'Ace':
            self.aceHit()
        elif card.value == 'King' or card.value == 'Queen' or card.value == 'Jack':
            self.total += 10
        else:
            self.total += card.value
        self.didBust()
        card.show()

    def stand(self):
        pass

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