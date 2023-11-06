from gamebrain import GameBrain
from gameboard import GameBoard
from player import Player

SIZE = 3 # Size of gameboard being played
PLAYERS = 2 # Number of players playing. Max 4


def player_turn(player:Player):
    """
    player_turn handles the steps and choices carried out for each player turn
    """
    pass


def play_game(enableAI:bool):
    """
    play_game initializes a new GameBoard object and begins the gameplay loop anew
    """
    brain = GameBrain()

    game_over = False
    players = brain.init_players(PLAYERS)
    turn = 1
    while not game_over:
        game_board = GameBoard(SIZE)
        game_board.print_game()



        player_turn(players[1+turn])

        # TODO: need to come up with turn rotation method. Maybe a double loop with inner looping players array
        turn += (1*-1)

        game_over = True


play_game(enableAI=True)
