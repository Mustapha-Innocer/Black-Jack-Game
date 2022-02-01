from .player_status import PlayerStatus


def strategy(player):
    if player.total() < 17:
        player.status = PlayerStatus.HIT
    elif player.total() > 21:
        player.status = PlayerStatus.GO_BUST
