import deck, card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.total = 0

    def showHand(self):
        print(self.name, "'s hand:")
        for card in self.hand:
            card.show()
        print('HAND TOTAL: ', self.total)

    def drawCard(self, deck):
        card = deck.draw()
        self.hand.append(card)
        return card

