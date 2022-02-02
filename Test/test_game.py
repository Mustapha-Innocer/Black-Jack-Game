from black_jack import game
from black_jack.Card import Card
from black_jack.player import Player
from unittest import TestCase


class TestGame(TestCase):
    def test_game_end_at_21(self):
        card1 = Card("heart", "10")
        card2 = Card("heart", "ace")
        player1 = Player("James", card1, card2)

        card3 = Card("diamond", "10")
        card4 = Card("diamond", "2")
        player2 = Player("John", card3, card4)

        players = [player1,player2]
        game.play(players)
        self.assertTrue(any([player.total() == 21 for player in players]))

