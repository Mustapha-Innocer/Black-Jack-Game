

from unittest import TestCase

from black_jack import strategy
from black_jack.Card import Card
from black_jack.player import Player
from black_jack.player_status import PlayerStatus


class TestStrategy(TestCase):
    def test_hit(self):
        card1 = Card("heart", "10")
        card2 = Card("heart", "2")
        player = Player("James", card1, card2)
        strategy.strategy(player)
        expected_status = PlayerStatus.HIT
        self.assertEqual(player.status, expected_status)

    def test_go_bust(self):
        card1 = Card("heart", "ace")
        card2 = Card("diamond", "ace")
        player = Player("James", card1, card2)
        strategy.strategy(player)
        expected_status = PlayerStatus.GO_BUST
        self.assertEqual(player.status, expected_status)

    def test_stick(self):
        card1 = Card("heart", "ace")
        card2 = Card("diamond", "8")
        player = Player("James", card1, card2)
        strategy.strategy(player)
        expected_status = PlayerStatus.STICK
        self.assertEqual(player.status, expected_status)
