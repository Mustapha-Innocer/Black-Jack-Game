from black_jack.player import Player
from black_jack.strategy import strategy
from black_jack.Deck import Deck
from black_jack.player_status import PlayerStatus


def game(players, deck):
    while True:
        for player in players:
            print(player.name + " --------- " + str(player.total()))
        if any([player.total() == 21 for player in players]):
            break
        elif players and all([player.status == PlayerStatus.STICK for player in players]):
            break
        elif len(players) == 1:
            break
        else:
            strategy(players, deck)
            print("In progress")


def winner(players):
    while True:
        if len(players) == 1:
            return "\n" + players[0].name + " has won"
        elif any([player.total() == 21 for player in players]):
            output = "\n"
            for player in players:
                if player.total() == 21:
                    output += player.name + " has won\n"
            return output
        elif players and ([player.status == PlayerStatus.STICK for player in players]):
            highest_score = max([player.total() for player in players], default=0)
            output = "\n"
            for player in players:
                if player.total() == highest_score:
                    output += player.name + " has won\n"
            return output
        else:
            return "No winner"


def play(number_of_players):
    deck = Deck()
    deck.shuffle()
    players = []
    for i in range(1, number_of_players + 1):
        players.append(Player("Player" + str(i), deck.deal_card(), deck.deal_card()))
    game(players, deck)
    return winner(players)
