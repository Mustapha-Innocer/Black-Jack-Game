import random

from Card import Card
from Label import Label
from Suit import Suit


class Deck:

    def __init__(self):
        self.cards = [Card(suit, label) for suit in Suit.suits for label in Label.labels]

    def shuffle_cards(self):
        random.shuffle(self.cards)


my_deck = Deck()

print(len(my_deck.cards))

my_deck.shuffle_cards()

print(len(my_deck.cards))
