from black_jack import game
from black_jack.Card import Card
from black_jack.player import Player
from unittest import TestCase


class TestGame(TestCase):
    def test_game_end_at_21(self):
        player1 = Player("James", Card("heart", "10"), Card("heart", "ace"))
        player2 = Player("John", Card("diamond", "10"), Card("diamond", "2"))
        players = [player1, player2]
        game.play(players)
        self.assertEqual(game.play(players), None)

    def test_game_end_at_all_players_stick(self):
        player1 = Player("James", Card("heart", "8"), Card("club", "ace"))
        player2 = Player("John", Card("diamond", "10"), Card("diamond", "jack"))
        players = [player1, player2]
        self.assertEqual(game.play(players), None)

    def test_game_end_when_one_is_left(self):
        player1 = Player("James", Card("heart", "7"), Card("club", "ace"))
        player2 = Player("John", Card("diamond", "ace"), Card("spade", "ace"))
        players = [player1, player2]
        self.assertEqual(game.play(players), None)
