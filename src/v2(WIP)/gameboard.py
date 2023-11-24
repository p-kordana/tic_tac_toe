class GameBoard:
    def __init__(self, size:int):
        """Initializes new blank game board using size parameter
        
        Keyword arguments:
        size -- takes int to determine size of game board
        Return: Boolean - True if initialization was correct.
        """
        if size < 3:
            print('SIZE provided was too small. Minimum is 3.\nExiting game. Correct the size and try again.')
            return False
        else:
            self.size = size
            self.board = [[' ' for _ in range(size)] for _ in range(size)]
            return True

    def print_board(self):
        """
        Print out a visual representation of the game board.
        """
        output_string = '   |'
        for x in range(self.size):
            output_string += f' {x+1} |'
        output_string += f'\n----{"----" * self.size}\n'  
        for r in range(self.size):
            output_string += f' {r+1} |'  
            for c in self.board[r]:
                output_string += f' {c} |'  
            output_string += f'\n----{"----" * self.size}\n'  
        print(output_string)

    def evaluate_board(self)->int:
        """Evalutes board for end of game conditions.
        
        Keyword arguments:
        argument -- description
        Return: integer (0=Draw, 1=Player 1 won, 2=Player 2 won)
        """
        self.check_for_win()
        self.check_for_draw()
        


    def check_for_draw(self)->bool:
        """
        Returns True if no free cells left aka. draw condition.
        Assumes that you have already evaluated for a win condition.
        """
        ctr = 0
        for r in self.board:
            for c in r:
                if c > " ":
                    ctr += 1
        if ctr == (self.size*self.size):
            return True
        return False

    def check_for_win(self, symbol:str)->bool:
        # set size and board variables in scope for repeated access
        s = self.size
        b = self.board
        
        ctr = 0
        # Check diagonal where x = y Ex: 0x0, 1x1, 2x2
        for x in range(s):
            c = b[x][x]
            if c == symbol:
                ctr += 1
        if ctr == s:
            return True
        
        ctr = 0
        # Check diagnol where y = SIZE-(x+1) Ex: 0x2, 1x1, 2x0
        for x in range(s):
            c = b[x][s-(x+1)]
            if c == symbol:
                ctr += 1
        if ctr == s:
            return True

        # Check verticals
        for v in range(s):
            ctr = 0
            for h in range(s):
                c = b[h][v]
                if c == symbol:
                    ctr += 1
            if ctr == s:
                return True

        # Check horizontals
        for h in range(s):
            ctr = 0
            for v in range(s):
                c = b[h][v]
                if c == symbol:
                    ctr += 1
            if ctr == s:
                return True
            
        return False

