from pprint import pprint

def find_next_empty(puzzle):
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == 0 :
                return row, column
    
    return None, None


def is_valid(puzzle, guess, row, col):
    row_values = puzzle[row]
    if guess in row_values:
        return False
    
    col_values = [puzzle[i][col] for i in range(9)]
    

    if guess in col_values:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for row in range(row_start, row_start + 3):
        for column in range(col_start, col_start + 3):
            if puzzle[row][column] == guess:
                return False

    return True


def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)

    if row is None:
        return True
    
    for guess in range(1,10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if solve_sudoku(puzzle):
                return True
            
        puzzle[row][col] = 0

    return False


if __name__ == '__main__':
    example_board = [
        [3, 9, 0,   0, 5, 0,   0, 0, 0],
        [0, 0, 0,   2, 0, 0,   0, 0, 5],
        [0, 0, 0,   7, 1, 9,   0, 8, 0],

        [0, 5, 0,   0, 6, 8,   0, 0, 0],
        [2, 0, 6,   0, 0, 3,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 4],

        [5, 0, 0,   0, 0, 0,   0, 0, 0],
        [6, 7, 0,   1, 0, 5,   0, 4, 0],
        [1, 0, 9,   0, 0, 0,   2, 0, 0]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)