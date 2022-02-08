from black_jack.game import game, winner, play
from black_jack.Card import Card
from black_jack.Deck import Deck
from black_jack.player import Player
from unittest import TestCase
from black_jack.player_status import PlayerStatus


class TestGame(TestCase):
    def test_game_end_at_21(self):
        deck = Deck()

        player1 = Player("James", Card("heart", "10"), Card("heart", "ace"))
        player2 = Player("John", Card("diamond", "10"), Card("diamond", "2"))
        players = [player1, player2]

        self.assertEqual(game(players, deck), None)

    def test_game_end_at_all_players_stick(self):

        deck = Deck()
        player1 = Player("James", Card("heart", "8"), Card("club", "ace"))
        player2 = Player("John", Card("diamond", "10"), Card("diamond", "jack"))

        players = [player1, player2]

        self.assertEqual(game(players, deck), None)

    def test_game_end_when_one_is_left(self):
        deck = Deck()

        player1 = Player("James", Card("heart", "7"), Card("club", "ace"))

        players = [player1]

        self.assertEqual(game(players, deck), None)

    def test_only_remaining_player_has_won(self):
        player1 = Player("James", Card("heart", "7"), Card("club", "ace"))

        players = [player1]

        self.assertEqual(winner(players), "\nJames has won")

    def test_players_with_exactly_21_have_won(self):
        player1 = Player("James", Card("heart", "10"), Card("club", "ace"))
        player2 = Player("John", Card("diamond", "10"), Card("diamond", "ace"))

        players = [player1, player2]

        expected_value = "\nJames has won\nJohn has won\n"

        self.assertEqual(winner(players), expected_value)

    def test_stick_players_with_highest_score_have_won(self):
        player1 = Player("James", Card("heart", "10"), Card("club", "9"))
        player2 = Player("John", Card("diamond", "10"), Card("diamond", "9"))
        player3 = Player("Ama", Card("club", "10"), Card("diamond", "8"))

        players = [player1, player2, player3]

        players[0].status = PlayerStatus.STICK
        players[1].status = PlayerStatus.STICK
        players[2].status = PlayerStatus.STICK

        expected_value = "\nJames has won\nJohn has won\n"
        self.assertEqual(winner(players), expected_value)

    def test_when_all_players_go_bust(self):
        player = []

        expected_value = "No winner"

        self.assertEqual(expected_value, winner(player))

    def test_game_plays_successfully(self):
        self.assertTrue(isinstance(play(5), str))
