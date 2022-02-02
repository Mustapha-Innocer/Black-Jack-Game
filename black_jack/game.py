def play(players):
    while True:
        if any([player.total() == 21 for player in players]):
            break
        print("In progress")
