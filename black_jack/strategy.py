from .player_status import PlayerStatus


def strategy(players, deck):
    for player in players:
        if player.total() < 17:
            player.status = PlayerStatus.HIT
            player.receive_card(deck.deal_card())
        elif player.total() > 21:
            players.remove(player)
        else:
            player.status = PlayerStatus.STICK
