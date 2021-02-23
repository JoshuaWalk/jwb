import blackjack_player 

class BlackjackDealer(blackjack_player.BlackjackPlayer):
    def __init__(self, name='Dealer'):
        self.name = name

    def turn(self):
        if self.total < 17:
            self.hit()
            self.turn()
        else:
            self.stand