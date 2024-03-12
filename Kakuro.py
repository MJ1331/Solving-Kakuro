def is_valid(board, row, col, num):
    # Check if 'num' is not already present in the current row and column
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False

    # Check if 'num' is not present in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_kakuro(board):
    empty_cell = find_empty_cell(board)

    # If no empty cell is found, the puzzle is solved
    if not empty_cell:
        return True

    row, col = empty_cell

    # Try filling in digits from 1 to 9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            # Recursively try to solve the puzzle
            if solve_kakuro(board):
                return True

            # If the current configuration leads to an invalid solution, backtrack
            board[row][col] = 0

    # No valid digit found, backtrack
    return False


def find_empty_cell(board):
    # Find the first empty cell in the board
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))


# Example Kakuro puzzle
kakuro_board = [
    [0, 0, 0, 3, 0, 0, 0, 4, 5],
    [0, 0, 0, 0, 4, 0, 0, 0, 6],
    [0, 5, 0, 0, 6, 0, 0, 0, 7],
    [6, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
    [4, 0, 0, 0, 0, 8, 0, 0, 0],
    [1, 2, 0, 0, 0, 0, 0, 0, 0]
]

print("Kakuro Puzzle:")
print_board(kakuro_board)
print("\nSolving...\n")

if solve_kakuro(kakuro_board):
    print("Solution:")
    print_board(kakuro_board)
else:
    print("No solution found.")
