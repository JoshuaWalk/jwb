import player, deck

class Game:
    def __init__(self, deck, *args):
        self.deck = deck
        self.players = list(*args)
    
    def addPlayer(self, player):
        self.players.append(player)

    def playRound(self):
        for player in self.players:
            player.turn()

    def showPlayers(self):
        for player in self.players:
            i = 1
            return 'Player {}'.format(i)

    