
## INTRODUCTION
Kakuro, also known as Cross Sums or Crosswords, is a logic-based puzzle game that combines elements of crossword puzzles and Sudoku. The objective of Kakuro is to fill in a grid with numbers from 1 to 9, similar to Sudoku, but with the additional constraint that the numbers must add up to specific target sums.

The Kakuro grid consists of blank white cells and shaded cells, where the shaded cells represent "clues" or "sums." Each clue consists of a number written in the shaded cell along with an arrow pointing either horizontally or vertically. The number represents the sum of the digits that should be placed in the adjacent white cells, either to the right or downwards from the clue.

The rules of Kakuro are as follows:

Each digit from 1 to 9 must appear exactly once in each row and each column, similar to Sudoku.
The digits placed in white cells must add up to the sum indicated by the corresponding clue.
A white cell cannot contain a zero.
Players use logic and deduction to determine which numbers should be placed in each white cell to satisfy both the sum constraints and the rules of Sudoku. The puzzle is solved when all white cells are filled in correctly, satisfying all the constraints.

Kakuro puzzles vary in difficulty, with smaller grids being simpler and larger grids offering more challenging gameplay. They require a combination of deductive reasoning, pattern recognition, and number manipulation skills to solve.

## IMPLEMENTATION
We use the following function to solve the problem
1. IS_VALID Function:
This function checks whether placing a number num at a given position (row, col) on the board is a valid move. It checks for conflicts in the same row, column, and 3x3 subgrid.
2. SOLVE_KAKURO Function:
This is the main recursive function that attempts to solve the Kakuro puzzle using backtracking. It finds the first empty cell using the find_empty_cell function. It iterates through the board and find first empty slot (i.e the slot with the value 0 ) to add the number. It tries filling in digits from 1 to 9 and recursively calls itself. If a valid solution is found, it returns True. Otherwise, it backtracks by setting the current cell to 0 and returns False.
3. PRINT_BOARD:
The print board function display the solution in a more understandable manner.
In summary, this code provides a basic implementation of a Kakuro puzzle solver using a backtracking algorithm. The solve_kakuro function is the core of the solution, and it employs recursive backtracking to explore possible solutions for the puzzle.




