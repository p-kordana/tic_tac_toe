from player import Player

class GameBrain:
    """
    GameBrain object;
    Manages players in array.
    Handles player setup with symbol selection.
    Keeps track of current player turn.
    """
    def __init__(self) -> None:
        self.players = [Player]
        self.symbols = []

    def init_players(self):

        count = input("How many players? Min 2, Max 4.")
        while not count in ['2','3','4']:
            print("Invalid input. Min 2, Max 4.")
            count = input("How many players?")
        count = int(count)

        for i in range(count):
            symbol = input(f"Player {i+1}. Select symbol")
            while symbol in self.symbols:
                print("Symbol already in use. Enter another.")
                symbol = input(f"Player {i+1}. Select symbol")
            self.symbols.append(symbol)
            self.players.append(Player(symbol))
