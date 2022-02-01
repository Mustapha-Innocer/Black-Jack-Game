import random

from .Card import Card
from .Label import Label
from .Suit import Suit


class Deck:
    def __init__(self):
        self.cards = [Card(suit, label) for suit in Suit.suits for label in Label.labels]
        self.shuffle()

    def __str__(self):
        cards_in_deck = ''
        for card in self.cards:
            cards_in_deck = cards_in_deck + str(card) + ' '
        return cards_in_deck

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        card = self.cards.pop(0)
        return card


my_deck = Deck()

print(my_deck)
