import pytest
from src.game import *
from src.deck import *
from src.blackjack_player import Player
from tests.params import name_list, full_name_list, player_names


@pytest.fixture
def deck():
    return Deck()

@pytest.fixture
def game(deck):
    return Game(deck)

@pytest.fixture
def game_with_players(deck):
    game = Game(deck, ['Josh', 'Kevin', 'Richard', 'Lindsey', 'Brandon'])
    game.init_players()
    return game
    
@pytest.fixture
def new_player():
    return Player('Frankie')

@pytest.mark.base
@pytest.mark.parametrize('name', player_names)
def test_add_player(name, game):
    game.add_player(name)
    assert game.show_players() == name

@pytest.mark.base
def test_add_player_full(game_with_players, new_player):
    game_with_players.add_player(new_player)
    assert game_with_players.show_players() == full_name_list

@pytest.mark.base
def test_player_list(game_with_players):
    assert game_with_players.show_players() == name_list

