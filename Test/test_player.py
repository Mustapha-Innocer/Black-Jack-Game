from unittest import TestCase
from black_jack.player import Player


class TestPlayer(TestCase):

    def setUp(self):
        self.player1 = Player("James")

    def test_set_status(self):
        self.assertEqual(self.player1.name, "James")
        self.assertEqual(self.player1.status, None)
        self.assertEqual(self.player1.count, 1)
