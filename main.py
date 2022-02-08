from black_jack.game import play
from sys import argv

num_of_players = 0
if len(argv) == 2:
    num_of_players = int(argv[1])
    if num_of_players < 2 or num_of_players > 6:
        num_of_players = 3
else:
    num_of_players = 3

print(play(num_of_players))
