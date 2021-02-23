import game

class Blackjack(game.Game):
    
    def playerTurn(self, decision):
        if decision == 'hit':
            self.hit()
            self.playerTurn()
        elif decision == 'stand':
            self.stand()


