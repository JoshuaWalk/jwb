import card

class Deck:
    def __init__(self, cards=[]):
        self.cards = cards
    
    def build(self):
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
        for suit in suits:
            for value in values:
                self.cards.append(card.Card(suit, value))

    def draw(self):
        return self.cards.pop
        
    def show(self):
        for card in self.cards:
            print(card.value, card.suit)
#deck = Deck()

#deck.build()
#deck.show()
