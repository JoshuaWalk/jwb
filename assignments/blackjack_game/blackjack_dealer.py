import blackjack_player 

class BlackjackDealer(blackjack_player.Player):
    def __init__(self):
        blackjack_player.Player.__init__(self, 'Dealer')


    def showHand(self):
        print("Dealer's Hand:")
        for card in self.hand:
            if len(self.hand) == 2 and card == self.hand[0]:
                print('hidden card')
                continue
            card.show()
        if len(self.hand) >= 3:
            print('HAND TOTAL: ', self.total, '\n')
