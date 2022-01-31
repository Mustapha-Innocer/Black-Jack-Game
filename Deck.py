import random

from Card import Card
from Label import Label
from Suit import Suit


class Deck:

    def __init__(self):
        self.cards = [Card(suit, label) for suit in Suit.suits for label in Label.labels]

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def deal_a_card(self):
        for i in range(2):
            self.cards.pop(0)

