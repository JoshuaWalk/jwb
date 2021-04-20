from src.blackjack_player import Player

class Game:
    def __init__(self, deck, *args):
        self.deck = deck
        self.players = [*args]
    
    def init_players(self):
        players = [Player(name) for name in self.players]
        self.players = players

    def add_player(self, player):
        self.players.append(Player(player))

    def show_players(self):
        for player in self.players:
            return player.name


