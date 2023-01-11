# sudoku solver agent
The game of sudoku is well known to many. You are given a 9x9 grid with some fixed values, and to solve the puzzle you must fill the empty cells of the grid such that the numbers 1 to 9 appear exactly once in each row, column, and 3x3 block of the grid.
### solver code
The file *sudoku.py* contains a function called *sudoku_solver* which takes one sudoku puzzle (a 9x9 NumPy array) as input, and returns the solved sudoku as another 9x9 NumPy array. This is done using a backtracking depth-first search with constraint propagation algorithm.
