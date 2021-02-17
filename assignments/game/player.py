import deck
print(deck)
class Player:
    def __init__(self):
        self.hand = []

    def showHand(self):
        for card in self.hand:
            card.show

    def drawCard(self, deck):
        card = deck.draw()
        print(deck)
        self.hand.append(card)
        return card

blackjack = deck.Deck()
player = Player()

blackjack.build()
player.drawCard(blackjack)
#player.showHand()