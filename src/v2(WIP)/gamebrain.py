from player import Player

# the allowed player symbols
symbols = ['X','O','|','-']

class GameBrain:
    players = [Player]
    def __init__(self) -> None:
        global players
        players = [Player]

    def init_players(self, count:int):
        for i in range(count):
            print(i)
            players.append(Player(symbols[i]))
