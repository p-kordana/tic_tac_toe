class Player:
    marker = ''

    def __init__(self, symbol) -> None:
        global marker
        marker = symbol
        self.wins = 0

    def add_win(self):
        self.wins += 1