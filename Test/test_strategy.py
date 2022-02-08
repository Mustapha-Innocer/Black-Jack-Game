from black_jack import strategy
from black_jack.Card import Card
from black_jack.Deck import Deck
from black_jack.player import Player
from black_jack.player_status import PlayerStatus
from unittest import TestCase


class TestStrategy(TestCase):
    def setUp(self) -> None:
        self.deck = Deck()

    def test_hit(self):
        player1 = Player("James", Card("heart", "10"), Card("heart", "2"))
        players = [player1]
        strategy.strategy(players, self.deck)
        expected_status = PlayerStatus.HIT
        self.assertEqual(players[0].status, expected_status)

    def test_go_bust(self):
        player1 = Player("James", Card("heart", "ace"), Card("diamond", "ace"))
        players = [player1]
        strategy.strategy(players,self.deck)
        self.assertTrue(len(players) == 0)

    def test_stick(self):
        player1 = Player("James", Card("heart", "ace"), Card("diamond", "8"))
        players = [player1]
        strategy.strategy(players, self.deck)
        expected_status = PlayerStatus.STICK
        self.assertEqual(players[0].status, expected_status)
