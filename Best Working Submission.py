import numpy as np

data = np.load("/data/very_easy_puzzle.npy")
solutions = np.load("/very_easy_solution.npy")
test_puzzle = data[14]
test2 = np.array([[3, 7, 4, 5, 8, 0, 6, 2, 9],
                  [8, 2, 5, 7, 9, 6, 4, 0, 1],
                  [6, 9, 1, 2, 3, 4, 8, 7, 5],
                  [1, 4, 2, 0, 5, 3, 7, 9, 8],
                  [7, 8, 6, 9, 4, 2, 1, 5, 3],
                  [9, 5, 3, 8, 1, 7, 2, 4, 6],
                  [4, 6, 9, 1, 7, 5, 3, 8, 2],
                  [5, 1, 7, 3, 2, 8, 0, 6, 4],
                  [2, 3, 8, 6, 0, 9, 5, 1, 7]])

test3 = np.array([[0, 8, 5, 0, 1, 3, 0, 0, 9],
                  [6, 3, 4, 0, 0, 2, 1, 7, 5],
                  [0, 2, 0, 5, 7, 4, 0, 3, 0],
                  [2, 4, 8, 3, 6, 7, 9, 5, 1],
                  [9, 6, 0, 4, 5, 8, 0, 2, 3],
                  [3, 5, 7, 2, 0, 0, 4, 8, 0],
                  [5, 7, 3, 1, 0, 0, 8, 9, 2],
                  [4, 9, 6, 0, 2, 5, 3, 1, 0],
                  [8, 1, 2, 0, 3, 9, 5, 6, 4]])

hard2 = np.array([[0, 2, 0, 0, 0, 6, 9, 0, 0],
                  [0, 0, 0, 0, 5, 0, 0, 2, 0],
                  [6, 0, 0, 3, 0, 0, 0, 0, 0],
                  [9, 4, 0, 0, 0, 7, 0, 0, 0],
                  [0, 0, 0, 4, 0, 0, 7, 0, 0],
                  [0, 3, 0, 2, 0, 0, 0, 8, 0],
                  [0, 0, 9, 0, 4, 0, 0, 0, 0],
                  [3, 0, 0, 9, 0, 2, 0, 1, 7],
                  [0, 0, 8, 0, 0, 0, 0, 0, 2]])

hard3 = np.array([[0, 0, 0, 0, 0, 0, 0, 5, 0],
                  [2, 0, 7, 0, 0, 9, 0, 0, 0],
                  [6, 0, 0, 3, 5, 1, 0, 0, 0],
                  [5, 0, 0, 0, 0, 0, 0, 1, 0],
                  [0, 0, 3, 0, 0, 0, 0, 0, 8],
                  [0, 0, 0, 8, 2, 0, 5, 3, 0],
                  [0, 0, 0, 0, 7, 0, 8, 0, 4],
                  [0, 0, 6, 2, 0, 0, 0, 0, 0],
                  [0, 8, 0, 0, 0, 0, 7, 0, 0]])


class SudokuState:
    def __init__(self, puzzle):
        self.empties = None
        self.state = puzzle
        self.state_dict = {}

    # checks if the state contains any remaining zeros, and if not then returns True to confirm that it is a goal state
    def is_goal(self):
        return np.all(self.state > 0)

    # checks if the indexed location contains a valid value
    def is_valid(self, row, col, val):
        if val not in self.state[(row - row % 3): (row - row % 3) + 3,
                      (col - col % 3): (col - col % 3) + 3] and val not in self.state[row][:] and val not in self.state[
                                                                                                             :, col]:
            return True
        else:
            return False

    # checks the indexed value against the contents of its row, column, and puzzle square, returning a list of values
    # (1-9) not present
    def get_possible_values(self, row, col):
        all_values = range(1, 10)
        poss_vals = ()
        for j in all_values:
            if j not in self.state[(row - row % 3): (row - row % 3) + 3,
                        (col - col % 3): (col - col % 3) + 3] and j not in self.state[row][:] and j not in self.state[:,
                                                                                                           col]:
                poss_vals = poss_vals + (j,)
        return poss_vals

    # sets the indexed value in the puzzle to a new value
    def set_value(self, row, col, val):
        self.state[row][col] = val

    # function to set the indexed value to zero when the incorrect value has been applied
    def set_zero(self, row, col):
        self.state[row][col] = 0

    # returns array of empty values
    def get_empty(self):
        self.empties = np.where(self.state == 0)
        return self.empties

    # returns value at given index
    def get_value(self, row, col):
        return self.state[row][col]

    # creates a dictionary where keys are an index tuple of missing variables, and the values are a list of possible
    # values
    def get_dict(self):
        for i in range(0, len(SudokuState.get_empty(self)[0])):
            self.state_dict[(SudokuState.get_empty(self)[0][i].item(),
                             SudokuState.get_empty(self)[1][i].item())] = SudokuState.get_possible_values(
                self, SudokuState.get_empty(self)[0][i].item(), SudokuState.get_empty(self)[1][i].item())
        return self.state_dict

    def __lt__(self, other):
        return self.state < other.state

    def __gt__(self, other):
        return self.state > other.state

    def __ge__(self, other):
        return self.state >= other.state

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.state.dict == other.state.dict)

    def __hash__(self):
        return hash(self.state)


first = True
last_attempt = []
tried_dict = {}


def add_to_tried(row, col, value=None):
    if value is not None:
        val = [value]
        if val not in tried_dict[(row, col)]:
            tried_dict[(row, col)] += val
    if (row, col) not in tried_dict:
        tried_dict[(row, col)] = []


def check_tried(key, value):
    if value in tried_dict[key]:
        return True


# get the keys of the last item tried in the tried dictionary
def get_last(keys):
    ind = list(tried_dict.keys()).index(keys)
    keys_list = list(tried_dict)
    return keys_list[ind - 1]


# Returns list of keys of input dictionary ordered by value tuple length greater than 0. If all length 0,
# returns list of keys.
def get_shortest_value(d):
    sorted_zeros = sorted(d, key=lambda ke: len(d[ke]), reverse=False)
    return sorted_zeros


# Function returns True if it can solve the Sudoku, or False if not.
def checker(sudoku):
    puzzle = SudokuState(sudoku)
    global first
    state_dict = {}
    state_dict.clear()
    state_dict = puzzle.get_dict()
    global last_attempt
    global tried_dict

    # while there are missing values with either one or no possible values, either return failure if no values are
    # found or set the value for those with only one possibility. Recreate the possible values dictionary and rerun
    # the check, filling in single values until none remain.
    if first:
        while any(len(value) <= 1 for value in state_dict.values()):
            for item in state_dict.items():
                if len(item[1]) == 0:
                    return False
                elif len(item[1]) == 1:
                    puzzle.set_value(item[0][0], item[0][1], item[1][0])
            if puzzle.is_goal():
                for i in range(0, len(puzzle.state)):
                    a, b = np.unique(puzzle.state[i, :], return_counts=True)
                    c, d = np.unique(puzzle.state[:, i], return_counts=True)
                    if np.any(b > 1) or np.any(d > 1):
                        return False
                    else:
                        pass
                return True
            else:
                state_dict.clear()
                state_dict = puzzle.get_dict()

    first = False

    if puzzle.is_goal():
        return True

    if not puzzle.is_goal():
        for key in get_shortest_value(state_dict):
            for v in state_dict[key]:
                if puzzle.is_valid(key[0], key[1], v):
                    puzzle.set_value(key[0], key[1], v)
                    if checker(puzzle.state):
                        return True
                    puzzle.set_zero(key[0], key[1])
            return False


def sudoku_solver(sudoku):
    if checker(sudoku):
        return sudoku
    else:
        return np.array([-1] * 81).reshape((9, 9))


if __name__ == "__main__":
    # print(SudokuState(test_puzzle).empty_values)
    # print(SudokuState(test_puzzle).get_possible_values(1, 1))
    # print(SudokuState(test_puzzle).is_goal())
    # print(SudokuState(test3).get_empty())
    print(hard3)
    print(sudoku_solver(test_puzzle))
