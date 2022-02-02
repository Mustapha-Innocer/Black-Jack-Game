from black_jack import game
from black_jack.Card import Card
from black_jack.player import Player
from unittest import TestCase

from black_jack.player_status import PlayerStatus


class TestGame(TestCase):
    def test_game_end_at_21(self):
        player1 = Player("James", Card("heart", "10"), Card("heart", "ace"))
        player2 = Player("John", Card("diamond", "10"), Card("diamond", "2"))
        players = [player1, player2]
        game.play(players)
        self.assertTrue(any([player.total() == 21 for player in players]))

    def test_game_end_at_all_players_stick(self):
        player1 = Player("James", Card("heart", "8"), Card("club", "ace"))
        player2 = Player("John", Card("diamond", "10"), Card("diamond", "jack"))
        players = [player1, player2]
        print(all([player.status == PlayerStatus.STICK for player in players]))
        game.play(players)
        self.assertTrue(all([player.status == PlayerStatus.STICK for player in players]))
