SIZE = 3 # Game board size (can be adjusted)

# Create GAMEBOARD and PLAYERS lists
GAMEBOARD = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]
PLAYERS = [
    {
        "name": "Player X",
        "symbol": "X",
        "wins": 0
    },
    {
        "name": "Player O",
        "symbol": "O",
        "wins": 0
    }
]

def init_gameboard():
    """Clears GAMEBOARD
    """
    global GAMEBOARD
    GAMEBOARD = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]

def print_gameboard():
    output_string = '   |'
    for x in range(SIZE):
        output_string += f' {x+1} |'
    output_string += f'\n----{"----" * SIZE}\n'  
    for r in range(SIZE):
        output_string += f' {r+1} |'  
        for c in GAMEBOARD[r]:
            output_string += f' {c} |'  
        output_string += f'\n----{"----" * SIZE}\n'  
    print(output_string)


def print_score(players):
    print("------------------")
    for p in players:
        print(f'{p["name"]}: {p["wins"]}')
    print("------------------")

def evaluate_selection(row:int, col:int)->bool:
    if GAMEBOARD[row-1][col-1] == ' ':
        return True
    else: 
        return False
    

def mark_selection(row:int, col:int, symbol:str):
    GAMEBOARD[row-1][col-1] = symbol


def check_for_draw()->bool:
    ctr = 0
    for r in GAMEBOARD:
        for c in r:
            if c > " ":
                ctr += 1
    if ctr == (SIZE*SIZE):
        return True
    return False


def check_for_win(symbol:str)->bool:
    ctr = 0
    # Check diagonal where x = y Ex: 0x0, 1x1, 2x2
    for x in range(SIZE):
        c = GAMEBOARD[x][x]
        if c == symbol:
            ctr += 1
        else:
            pass
    if ctr == SIZE:
        return True
    
    ctr = 0
    # Check diagnol where y = SIZE-(x+1) Ex: 0x2, 1x1, 2x0
    for x in range(SIZE):
        c = GAMEBOARD[x][SIZE-(x+1)]
        if c == symbol:
            ctr += 1
        else:
            pass
    if ctr == SIZE:
        return True

    # Check verticals
    for v in range(SIZE):
        ctr = 0
        for h in range(SIZE):
            c = GAMEBOARD[h][v]
            if c == symbol:
                ctr += 1
        if ctr == SIZE:
            return True

    # Check horizontals
    for h in range(SIZE):
        ctr = 0
        for v in range(SIZE):
            c = GAMEBOARD[h][v]
            if c == symbol:
                ctr += 1
        if ctr == SIZE:
            return True
        
    return False

done_playing = False
game_over = False

while not done_playing:
    while not game_over:
        for player in PLAYERS:
            if not game_over:
                print_gameboard()
                # Load name and symbol into variables for easier references
                pn = player['name']
                ps = player['symbol']

                print(f"{pn}'s turn.")

                try_again = True
                # Loop continues until player makes valid row & column selection
                while try_again:
                    row_not_int = True
                    while row_not_int:
                        try:
                            # Try to convert user input to an integer
                            row = input('Select row: ')
                            row = int(row)
                        except ValueError:
                            # If a ValueError occurs (e.g., if the input is not a valid integer), handle it here
                            print("Invalid input. Please enter a valid integer.")
                        else:
                            if row in range(1,SIZE+1):
                                # If no exception break out of loop
                                row_not_int = False
                            else:
                                print(f'Invalid input. Must be between 1 and {SIZE}.')

                    col_not_int = True
                    while col_not_int:
                        try:
                            # Try to convert user input to an integer
                            col = input('Select column: ')
                            col = int(col)
                        except ValueError:
                            # If a ValueError occurs (e.g., if the input is not a valid integer), handle it here
                            print("Invalid input. Please enter a valid integer.")
                        else:
                            if col in range(1,SIZE+1):
                                # If no exception break out of loop
                                col_not_int = False
                            else:
                                print(f'Invalid input. Must be between 1 and {SIZE}.')

                    try_again = not evaluate_selection(row, col)
                    if try_again:
                        print("Invalid selection. Try again.")

                mark_selection(row, col, ps)
                player_wins = check_for_win(ps)
                if player_wins:
                    print_gameboard()
                    player['wins'] += 1
                    print(f'{pn} wins!'.upper())
                    game_over = True
                else: 
                    if check_for_draw():
                        print_gameboard()
                        print('No moves left. Draw!')
                        game_over = True

    ans = ''
    while not ans in ['Y','N']:
        ans = input('Play again? Y or N: ').upper()
    if ans == 'N':
        # If done playing set bool to break loop and print final scores
        done_playing = True
        print_score(PLAYERS)
    else:
        # Else re-init the gameboard and unset game over bool to continue game loop
        init_gameboard()
        game_over = False
        print(f'\n') # Add new line for next game


