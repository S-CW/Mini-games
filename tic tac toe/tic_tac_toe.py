import math, random, time

class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random empty spot for our next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0 - 8): ")
            # Check for empty spot using val int
            # If spot is not available on board, an invalid is raise
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # If there is an empty spot
            except ValueError:
                print("Invalid square. Try again")

        return val

class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
            return square
    
    def minimax(self, state, player):
        max_player = self.letter # yourself
        other_player = 'O' if player == 'X' else 'X' # defining other player letter

        if state.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
            }

        elif not state.empty_squares(): # no empty squares
            return {
                'position': None,
                'score': 0
            }

        # initialize some dictionaries // starting score
        if player == max_player:
            best = {
                'position': None,
                'score': -math.inf # each score should maximize(be larger) replacing the previous score
            }
        else:
            best = {
                'position': None,
                'score': math.inf # each score should minimize
            }

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # step 2: recurse using minimax  to simulate the next possible move
            sim_score = self.minimax(state, other_player) # alternate player

            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            # step 4: update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best



##### Initialize game #####
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # List to represent 3x3 board
        self.current_winner = None # Keep track of winner!

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_num():
        # 0 | 1 | 2 etc (tells what number corresponds to what box)
        num_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in num_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
         return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check row
        row_ind = math.floor(square // 3)
        row = self.board[row_ind*3: (row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True
        
        # check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in diagonal2):
                return True

        # If all fails then 
        return False


def play(game, x_player, o_player, print_game=True):
    # return the winner of the game! or None as a tie
    if print_game:
        game.print_board_num()

    letter = 'X' # starting letter 
    while game.empty_squares():
        # get move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # define function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print('') # just empty line

            if game.current_winner:
                if print_game:
                    print(letter + " won!")
                return letter

            # after make a move, alternate letter for other player to make a move
            letter = 'O' if letter == 'X' else 'X'

    time.sleep(0.8)
    

    print("It's a tie!")



if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = SmartComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

