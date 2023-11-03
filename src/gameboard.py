class GameBoard:
    def __init__(self, size:int):
        """initializes new blank game board using size parameter
        
        Keyword arguments:
        size -- takes int to determine size of game board
        Return: none
        """
        self.size = size
        self.game_board = [[' ' for _ in range(size)] for _ in range(size)]

    def print_game(self):
        """
        Print out a visual representation of the game board.
        :return:
        """
        output_string = f'-{"----" * self.size}\n'  # Append top line
        for r in self.game_board:
            output_string += '|'  # Append vertical line before each row
            for c in r:
                output_string += f' {c} |'  # Pad spaces around each col value
            output_string += f'\n-{"----" * self.size}\n'  # Append row underlines
        print(output_string)
