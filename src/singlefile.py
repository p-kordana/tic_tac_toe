# Game board size (can be adjusted) 
# Note that SIZE > 3 becomes much harder for players to win.
SIZE = 3

# Create GAMEBOARD and PLAYERS lists
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

def init_gameboard(size:int)->bool:
    """
    Clears global GAMEBOARD variable
    """
    if size < 3:
        print('SIZE provided was too small. Minimum is 3.\nExiting game. Correct the size and try again.')
        return False
    else:
        global GAMEBOARD
        GAMEBOARD = [[' ' for _ in range(size)] for _ in range(size)]
        return True

def print_gameboard():
    """
    Prints text represenation of the global GAMEBOARD array to stdout
    """
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
    """
    Prints text scoreboard for player wins
    """
    print("------------------")
    for p in players:
        print(f'{p["name"]}: {p["wins"]}')
    print("------------------")


def select_row()->int:
    """
    Evaluates player row selection and returns int once complete.
    """
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
    return row

def select_col()->int:
    """
    Evaluates player col selection and returns int once complete.
    """
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
    return col

def evaluate_selection(row:int, col:int)->bool:
    """
    Evaluates selected cell and returns false if not valid.\n
    This is only used after select_row() and select_col() have evaluated selection within the board.
    """
    if GAMEBOARD[row-1][col-1] == ' ':
        return True
    else: 
        return False
    

def mark_selection(row:int, col:int, symbol:str):
    """
    Adds player symbol in the evaluated, selected, cell.
    """
    GAMEBOARD[row-1][col-1] = symbol


def check_for_draw()->bool:
    """
    Returns True if no free cells left aka. draw condition.
    Assumes that you have already evaluated for a win condition.
    """
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
    if ctr == SIZE:
        return True
    
    ctr = 0
    # Check diagnol where y = SIZE-(x+1) Ex: 0x2, 1x1, 2x0
    for x in range(SIZE):
        c = GAMEBOARD[x][SIZE-(x+1)]
        if c == symbol:
            ctr += 1
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

    if not init_gameboard(SIZE):
        game_over = True
        break

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
                    row = select_row()
                    col = select_col()

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
        # Else unset game over bool to continue game loop
        game_over = False
        print(f'\n') # Add new line for next game


