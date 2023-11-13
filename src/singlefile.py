SIZE = 4 # Game board size (can be adjusted)

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
                player_wins = check_for_win(ps)
                if player_wins:
                    print_gameboard()
                    player['wins'] += 1
                    print(f'{pn} wins!'.upper())
                    print_score(PLAYERS)
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
        done_playing = True
    else:
        init_gameboard()
        game_over = False


