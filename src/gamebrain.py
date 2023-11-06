from player import Player

symbols = ['X','O','|','-']

class GameBrain:
    def __init__(self) -> None:
        self.players = [Player]

    def init_players(self, count:int)->[Player]:
        for i in range(count):
            self.players.append(Player(symbols[i]))
        return self.players