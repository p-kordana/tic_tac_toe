from gameboard import GameBoard

SIZE = 3 # Size of gameboard being played

# TODO: Lay out a player turn (How to select row and column?)
# TODO: Determine how AI player functions (Random? Strategy?)
# TODO: Write check_for_win method (needs to account for diagonal and verticals)


def check_for_win():
    """
    Diagonal wins can only be from corner to corner (Check both diagonals)
        0x0, 1x1, 2x2 | 0x2, 1x1, 2x0
    Vertical wins when same value in a single Column (Loop check all columns)
        0x0, 1x0, 2x0 | 0x1, 1x1, 2x1 | 0x2, 1x2, 2x2
    Horizontal wins when same value in a single Row (Loop check all rows)
        0x0, 0x1, 0x2 | 1x0, 1x1, 1x2 | 2x0, 2x1, 2x2
    False on first value difference when checking
    """
    
    pass


def player_turn():
    """
    player_turn handles the steps and choices carried out for each player turn
    """
    pass


def play_game(enableAI:bool):
    """
    play_game initializes a new GameBoard object and begins the gameplay loop anew
    """
    game_over = False

    while not game_over:
        game_board = GameBoard(SIZE)
        game_board.print_game()

        game_over = True


play_game(enableAI=True)
