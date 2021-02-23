import deck, card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.total = 0

    def showHand(self):
        for card in self.hand:
            print(card.show())

    def drawCard(self, deck):
        card = deck.draw()
        self.hand.append(card)
        return card

