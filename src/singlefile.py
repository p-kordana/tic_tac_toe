SIZE = 3 # Game board size (can be adjusted)

# Create GAMEBOARD and PLAYERS lists
GAMEBOARD = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]
PLAYERS = [
    {
        "name": "Player 1",
        "symbol": "X",
        "wins": 0
    },
    {
        "name": "Player 2",
        "symbol": "O",
        "wins": 0
    }
]

def print_gameboard():
    output_string = f'-{"----" * SIZE}\n'  # Append top line
    for r in GAMEBOARD:
        output_string += '|'  # Append vertical line before each row
        for c in r:
            output_string += f' {c} |'  # Pad spaces around each col value
        output_string += f'\n-{"----" * SIZE}\n'  # Append row underlines
    print(output_string)


def evaluate_selection(row:int, col:int)->bool:
    if GAMEBOARD[row-1][col-1] == ' ':
        return True
    else: 
        return False
    

def mark_selection(row:int, col:int, symbol:str):
    GAMEBOARD[row-1][col-1] = symbol


def check_for_win(symbol:str)->bool:
    """
    Diagonal wins can only be from corner to corner (Check both diagonals)
        0x0, 1x1, 2x2 | 0x2, 1x1, 2x0
    Vertical wins when same value in a single Column (Loop check all columns)
        0x0, 1x0, 2x0 | 0x1, 1x1, 2x1 | 0x2, 1x2, 2x2
    Horizontal wins when same value in a single Row (Loop check all rows)
        0x0, 0x1, 0x2 | 1x0, 1x1, 1x2 | 2x0, 2x1, 2x2
    False on first value difference when checking
    """
    ctr = 0
    win = False
    # Check diagonal where x = y
    for x in range(SIZE):
        ctr = 0
        c = GAMEBOARD[x][x]
        if c == symbol:
            ctr += 1
    if ctr == SIZE:
        win = True
        return
    # Check diagnol where y = -(x+1)
    for x in range(SIZE):
        ctr = 0
        c = GAMEBOARD[x][-(x+1)]
        if c == symbol:
            ctr += 1
    if ctr == SIZE:
        win = True
        return

    # Check verticals
    for v in range(SIZE):
        ctr = 0
        for h in range(SIZE):
            c = GAMEBOARD[h][v]
            if c == symbol:
                ctr += 1
        if ctr == SIZE:
            win = True
            return

    # Check horizontals
    for h in range(SIZE):
        ctr = 0
        for v in range(SIZE):
            c = GAMEBOARD[h][v]
            if c == symbol:
                ctr += 1
        if ctr == SIZE:
            win = True
            return
    if win:
        print(f'Player "{symbol}" wins!')

    return win

game_over = False

while not game_over:
    for player in PLAYERS:
        if not game_over:
            print_gameboard()
            # Load name and symbol into variables for easier references
            pn = player['name']
            ps = player['symbol']

            print(f"{pn}'s turn.")
            row = input('Select row: ')
            col = input('Select column: ')
            # Loop continues until player makes valid row & column selection
            while not evaluate_selection(int(row), int(col)):
                print(f'Invalid selection. {pn} Try again.')
                row = input('Select row: ')
                col = input('Select column: ')
            row = int(row)
            col = int(col)
            mark_selection(row, col, ps)
            game_over = check_for_win(ps)


