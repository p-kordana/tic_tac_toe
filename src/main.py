from gameboard import GameBoard


def check_for_wins():
    pass


def player_turn():
    """
    player_turn handles the steps and choices carried out for each player turn
    :return:
    """
    pass


def play_game(enableAI:bool):
    """
    play_game initializes a new GameBoard object and begins the gameplay loop anew
    :return:
    """
    game_over = False

    while not game_over:
        game_board = GameBoard()
        game_board.print_game()

        game_over = True


play_game(enableAI=True)
