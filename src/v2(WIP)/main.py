from gamebrain import GameBrain
from gameboard import GameBoard
from player import Player

SIZE = 3 # Size of gameboard being played
PLAYERS = 2 # Number of players playing. Max 4


def player_turn(player:Player):
    """
    player_turn handles the steps and choices carried out for each player turn
    """
    print(f'Player {player.marker} turn')
    # TODO: Add a loop with integer checking on both row and col
    try: 
        row = int(input('Select a row: '))
    except:
        pass

    try:
        col = int(input('Select a column: '))
    except:
        pass



def play_game(enableAI:bool):
    """
    play_game initializes a new GameBoard object and begins the gameplay loop anew
    """
    brain = GameBrain()

    game_over = False
    brain.init_players(PLAYERS)
    game_board = GameBoard(SIZE)

    while not game_over:
        game_board.print_game()

        for player in brain.players:
            player_turn(player)

        game_over = True


play_game(enableAI=True)
