class Player:
    def __init__(self, symbol) -> None:
        self.symbol = symbol
        self.wins = 0

    def add_win(self):
        self.wins += 1