import unittest
from black_jack.Deck import Deck


class MainTest(unittest.TestCase):
    def test_deal_card(self):
        # given
        expected = 51

        # when
        my_deck = Deck()
        my_deck.deal_card()

        # then
        self.assertEqual(expected, len(my_deck.cards))

    def test_create_deck_of_card(self):
        # given
        expected = 52

        # when
        my_deck = Deck()

        # then
        self.assertEqual(expected, len(my_deck.cards))
