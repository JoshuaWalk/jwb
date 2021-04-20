import pytest
from src.game import *
from src.deck import *
from src.blackjack_player import Player
from tests.params import name_list, full_name_list, player_names

@pytest.fixture
def game_deck():
    deck = Deck()
    deck.build()
    return deck

@pytest.fixture
def empty_game(game_deck):
    return Game(game_deck)

@pytest.fixture
def game_with_players(game_deck):
    game = Game(game_deck, ['Josh', 'Kevin', 'Richard', 'Lindsey', 'Brandon'])
    game.init_players()
    return game

@pytest.mark.base
@pytest.mark.parametrize('name', player_names)
def test_add_player(name, empty_game):
    empty_game.add_player(name)
    assert empty_game.show_players() == name

@pytest.mark.base
def test_player_list(game_with_players):
    assert game_with_players.show_players() == name_list

@pytest.mark.base
def test_add_player_full(game_with_players):
    game_with_players.add_player('Frankie')
    assert game_with_players.show_players() == full_name_list