from .player_status import PlayerStatus


def strategy(player):
    if player.total() < 17:
        player.status = PlayerStatus.HIT
