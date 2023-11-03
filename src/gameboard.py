ROWS = 3
COLS = 3


class GameBoard:
    def __init__(self):
        """
        initializes new blank game board using ROWS and COLS constants
        """
        self.game_board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]

    def print_game(self):
        """
        Print out a visual representation of the game board.
        :return:
        """
        output_string = f'-{"----" * COLS}\n'  # Append top line
        for r in self.game_board:
            output_string += '|'  # Append vertical line before each row
            for c in r:
                output_string += f' {c} |'  # Pad spaces around each col value
            output_string += f'\n-{"----" * COLS}\n'  # Append row underlines
        print(output_string)
