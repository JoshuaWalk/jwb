import card, random

class Deck:
    def __init__(self):
        self.cards = []
    
    def build(self):
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
        for s in suits:
            for v in values:
                self.cards.append(card.Card(s, v))

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        print('shuffling cards\n')
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, len(self.cards)-1)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    
    def clear(self):
        self.cards = []
        
    def show(self):
        for card in self.cards:
            print(card.value, card.suit)


