import random

class Card:
    """
    attributes:\n
        suit (str),
        value (str/num),
        is_used (bool),

    methods:\n
        show - prints suit and value of card
    """
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.is_used = False

    def show(self):
        print(f'{self.value} of {self.suit}')



class Deck:
    """
    attributes:
        cards (list)

    methods:
        build - creates a standard 52 card deck
        shuffle - arranges the cards in random order
        clear - removes all cards from deck
        draw - returns a card in an array
        show - prints every card in deck
    """
    def __init__(self):
        self.cards = []
    
    def build(self):
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
        for s in suits:
            for v in values:
                self.cards.append(Card(s, v))

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        print('shuffling cards\n')
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, len(self.cards)-1)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    
    def reset(self):
        self.cards = []
        self.build()
        self.shuffle()
        
    def show(self):
        for card in self.cards:
            print(card.value, card.suit)

