from black_jack import strategy
from black_jack.Card import Card
from black_jack.player import Player
from black_jack.player_status import PlayerStatus
from unittest import TestCase


class TestStrategy(TestCase):
    def test_hit(self):
        players = [
            Player("James", Card("heart", "10"), Card("heart", "2"))
        ]
        strategy.strategy(players)
        expected_status = PlayerStatus.HIT
        self.assertEqual(players[0].status, expected_status)

    def test_go_bust(self):
        players = [
            Player("James", Card("heart", "ace"), Card("diamond", "ace"))
        ]

        strategy.strategy(players)
        self.assertTrue(len(players) == 0)

    def test_stick(self):
        players = [
            Player("James", Card("heart", "ace"), Card("diamond", "8"))
        ]
        strategy.strategy(players)
        expected_status = PlayerStatus.STICK
        self.assertEqual(players[0].status, expected_status)
