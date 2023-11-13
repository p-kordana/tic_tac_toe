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

    def check_for_win(self)->bool:
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: 
        """
        

        """
        Diagonal wins can only be from corner to corner (Check both diagonals)
            0x0, 1x1, 2x2 | 0x2, 1x1, 2x0
        Vertical wins when same value in a single Column (Loop check all columns)
            0x0, 1x0, 2x0 | 0x1, 1x1, 2x1 | 0x2, 1x2, 2x2
        Horizontal wins when same value in a single Row (Loop check all rows)
            0x0, 0x1, 0x2 | 1x0, 1x1, 1x2 | 2x0, 2x1, 2x2
        False on first value difference when checking
        """

        return False