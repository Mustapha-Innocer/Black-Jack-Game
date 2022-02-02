from black_jack import strategy
from black_jack.player_status import PlayerStatus


def play(players):
    while True:
        if any([player.total() == 21 for player in players]):
            break
        elif all([player.status == PlayerStatus.STICK for player in players]):
            break
        elif len(players) == 1:
            break
        print("In progress")
        strategy.strategy(players)

