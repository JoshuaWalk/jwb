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
        self.is_busted = False

    def showHand(self):
        print(self.name, "'s hand:")
        for card in self.hand:
            card.show()
        print('HAND TOTAL: ', self.total, '\n')

    def restart(self):
        self.hand = []
        self.total = 0
        self.is_busted = False


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
        print("\nDealer's Hand:")
        for card in self.hand:
            if self.hide_card == True:
                print('hidden card')
                self.hide_card = False
            else:
                card.show()

    def restart(self):
        self.hand = []
        self.total = 0
        self.is_busted = False
        self.hide_card = True