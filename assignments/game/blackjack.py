import game

class Blackjack(game.Game):
    
    def deal(self, deck):
        for player in self.players:
            if type(player).__name__ == 'BlackjackDealer':
                player.hiddenHit(deck)
            else:
                player.hit(deck)
        for player in self.players:
            player.hit(deck)

    def playerTurn(self, decision, deck):
        if decision == 'hit':
            self.hit(deck)
            self.playerTurn()
        elif decision == 'stand':
            self.stand()


