# create board object to represent the game
import random, re

from sqlalchemy import over


class Board:
    def __init__(self, dim_size, num_bombs):
        # keep track of these parameters
        self.dim_size = dim_size
        self.num_bomb = num_bombs

        # create board with helper function
        self.board = self.make_new_board()  # plant the bombs
        self.assign_values_to_board()


        # initialize a set to keep track of which locations we've uncovered
        # save (row, col) tuples into this set
        self.dug = set()    # if dig at 0, 0 then self.dug = {(0, 0)}

    def make_new_board(self):
        # construct a new board based on the dim size and num bombs
        # construct the list of list here (or whatever representation) as we have 2D board

        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this create an array like:
        # [[None, None, ..., None],
        # [None, None, ..., None],
        # [None, None, ..., None]]

        # plant the bomb
        bombs_planted = 0
        while bombs_planted < self.num_bomb:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size # the remainder gives information on index of the row

            if board[row][col] == '*':
                # this means a bomb is planted there already so keep going
                continue

            board[row][col] = '*' # plant the bombs
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighbouring_bombs(r, c)

    def get_num_neighbouring_bombs(self, row, col):
        # iterate through each of the neighboring positions and sum number bombs
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)

        num_neighbouring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    # original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighbouring_bombs += 1
                    
        return num_neighbouring_bombs

    def dig(self, row, col):
        # dig at location
        # return True if successful dig, false if bomb is dug

        # few scenarios:
        # hit a bomb --> game over
        # dig at location with neighboring bombs --> finish dig
        # dig at location with no neighboring bombs --> recursively dig neighbors

        self.dug.add((row, col)) # Keep track dug location

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        # self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue # don't dig at dug location
                self.dig(r, c)
        # if at initial dig didn't hit a bomb, here will not hit a bomb
        return True

    def __str__(self):
        # when call print, will print out what the function returns!
        # return a string showing the board to player

        # create a new array that represent what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep


# play the game
def play(dim_size=10, num_bombs=10):
    # Step 1: create board and plant bombs
    board = Board(dim_size, num_bombs)

    # Step 2: show user the board and ask for where they want to dig
    # Step 3a: if location is a bomb, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is atleast next to a bomb
    # Step 4: repeat step 2 and 3a/b until there are no more places to dig --> VICTORY!
    safe = True

    while len(board.dug) < board.dim_size**2 - num_bombs:
        print(board)

        user_input = re.split(',(\\s)*', input("Where would you want to dig? Input as row, col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue

        # if it's valid, we dig
        safe = board.dig(row, col)
        if not safe:
            # dug a bomb, game over!
            break
    
    # 2 ways to end loop
    if safe:
        print("CONGRATULATIONS!! YOU WON!!!")
    else:
        print("SORRY GAME OVER")
        # show current whole board
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)


if __name__ == '__main__':
    play()