import game, blackjack_player, blackjack_dealer 

class Blackjack(game.Game):
    def __init__(self, deck, *args):
        game.Game.__init__(self, deck, *args)
        self.winner = blackjack_dealer.BlackjackDealer()

    def deal(self, deck):
        for player in self.players:
            if type(player).__name__ == 'BlackjackDealer':
                print(player.name)
                player.hiddenHit(deck)
            else:
                print(player.name)
                player.hit(deck)
        for player in self.players:
            print(player.name)
            player.hit(deck)
    def determineWinner(self):
        for player in self.players:
            if player.total <= 21:
                if player.total < self.winner.total:
                    self.winner = player
        return self.winner.name

    def playerTurn(self, decision, deck):
        if decision == 'hit':
            self.hit(deck)
            self.playerTurn()
        elif decision == 'stand':
            self.stand()


