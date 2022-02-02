from unittest import TestCase

from black_jack.Card import Card
from black_jack.Deck import Deck
from black_jack.player import Player


class TestPlayer(TestCase):

    def setUp(self):
        self.deck = Deck()
        self.card = Card('heart', 4)
        self.player1 = Player("James", self.deck.deal_card(), self.deck.deal_card())

    def test_set_status(self):
        self.assertEqual(self.player1.name, "James")
        self.assertEqual(self.player1.status, None)
        self.assertEqual(self.player1.count, 1)

    def test_card_total(self):
        self.assertEqual(self.player1.total(), 5)

    def test_receive_card(self):
        self.player1.receive_card(self.card)
        self.assertEqual(len(self.player1.cards), 3)