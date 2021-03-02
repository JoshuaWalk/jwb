class Player:
    '''
    attributes:
        name (str)
        hand (list)
        total (num)
        isBusted (bool)
    
    methods:
        showHand - calls show method on every card in hand
    '''
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.total = 0
        self.isBusted = False

    def showHand(self):
        print(self.name, "'s hand:")
        for card in self.hand:
            card.show()
        print('HAND TOTAL: ', self.total, '\n')


class BlackjackDealer(Player):
    '''
    attributes:
        name (str)
        hand (list)
        total (num)
        isBusted (bool)
        hide_card (bool)
    
    methods:
        showHand - calls show method on every card in hand
    '''
    def __init__(self):
        Player.__init__(self, 'Dealer')
        self.hide_card = True


    def showHand(self):
        print("Dealer's Hand:")
        for card in self.hand:
            if self.hide_card == True:
                print('hidden card')
                self.hide_card = False
            card.show()