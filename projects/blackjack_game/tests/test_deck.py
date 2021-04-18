import pytest
from tests.params import *
from src.deck import Card, Deck

@pytest.fixture
def empty_deck():
    deck = Deck()
    return deck

@pytest.fixture
def first_deck():
    deck = Deck()
    deck.build()
    return deck

@pytest.fixture
def second_deck():
    deck = Deck()
    deck.build()
    return deck

@pytest.mark.card
@pytest.mark.parametrize("s, v, out", low_cards)
def test_show(s, v, out):
    card = Card(s, v)
    assert card.show() == out

@pytest.mark.deck
@pytest.mark.parametrize("s, v, out", low_cards)
def test_add(s, v, out, empty_deck):
    empty_deck.add_card(s, v)
    card = empty_deck.draw()
    assert card.show() == out

@pytest.mark.deck
def test_deck_length(first_deck):
    assert len(first_deck.cards) == 52


