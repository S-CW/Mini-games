from pprint import pprint

def find_next_empty(puzzle):
    # find the next row, col on the puzzle that's not filled yet --> rep with -1
    # return index of row, col in the list of lists which is the first empty else when there is no empty spacce return (Nonne. None)

    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9): # range(9) is 0, 1, 2, ... 8
            if puzzle[r][c] == -1:
                return r, c
    
    return None, None # if no spaces in the puzzle are empty(-1)

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at row/col of puzzle is a valid guess
    # returns True if is valid, False otherwise
    # if guess == row or col or in 3x3 square, it is not valid

    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # 3x3 square
    row_start = (row // 3) * 3 # the first row of each 3x3 square
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # if all condition set is pass
    return True
    

def solve_sudoku(puzzle):
    # solving sudoku using a backtracking technique
    # sudoku puzzle is a list of lists, where each inner list is a row in the sudoku puzzle
    # return whether a solution exists

    # step 1: choose somewhere on the puzzle
    row, col = find_next_empty(puzzle)

    # step 1.1: if no empty space left, finish solving the puzzle
    if row is None:
        return True
    
    # step 2: if there is a place to put number, then make a guess between 1 and 9
    for guess in range(1, 10):
        # step 3: check if this valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, place guess on the puzzle
            puzzle[row][col] = guess

            # step 4: recursively call function
            if solve_sudoku(puzzle):
                return "Sudoku solve!"

        # step 5: if not valid then backtrack and try new number
        puzzle[row][col] = -1   # reset the guess

    # step 6: if no number solution
    return False
        
if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
