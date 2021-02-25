import blackjack_player 

class BlackjackDealer(blackjack_player.BlackjackPlayer):
    def __init__(self):
        blackjack_player.BlackjackPlayer.__init__(self, 'Dealer')
        self.total = 0

    def showHand(self):
        for card in self.hand:
            if len(self.hand) == 2 and card == self.hand[0]:
                print('hidden card')
                continue
            card.show()
        if len(self.hand) >= 3:
            print('HAND TOTAL: ', self.total)
