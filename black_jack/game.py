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
        elif all([player.status == PlayerStatus.STICK for player in players]):
            break
        elif len(players) == 1:
            break
        strategy(players, deck)
        print("In progress")


def play(number_of_players):
    deck = Deck()
    deck.shuffle()
    players = []
    for i in range(1, number_of_players + 1):
        players.append(Player("Player" + str(i), deck.deal_card(), deck.deal_card()))

    game(players, deck)
    while True:
        if len(players) == 1:
            print("__________________________\n")
            print(players[0].name + " has won")
            break
        elif any([player.total() == 21 for player in players]):
            for player in players:
                if player.total() == 21:
                    print("\n__________________________")
                    print(player.name + " has won")
            break
        elif all([player.status == PlayerStatus.STICK for player in players]):
            highest_score = max([player.total() for player in players], default=0)
            for player in players:
                if player.total() == highest_score:
                    print("\n__________________________")
                    print(player.name + " has won")
            break
        else:
            print("No winner")
            break
