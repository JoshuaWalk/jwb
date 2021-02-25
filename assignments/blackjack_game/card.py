class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.status = False

    def show(self):
        print(f'{self.value} of {self.suit}')