import unittest
from Deck import Deck


class mainTest(unittest.TestCase):
    def test_deal_card(self):
        # given
        expected = 51

        # when
        myDeck = Deck()
        myDeck.deal_card()

        # then
        self.assertEqual(expected, len(myDeck.cards))

    def test_create_deck_of_card(self):
        # given
        expected = 52

        # when
        myDeck = Deck()

        # then
        self.assertEqual(expected, len(myDeck.cards))

