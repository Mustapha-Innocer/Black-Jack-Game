from .player_status import PlayerStatus


def strategy(players: list) -> None:
    for player in players:
        if player.total() < 17:
            player.status = PlayerStatus.HIT
        elif player.total() > 21:
            players.remove(player)
        else:
            player.status = PlayerStatus.STICK
