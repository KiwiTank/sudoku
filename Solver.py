import numpy as np

data = np.load("/data/very_easy_puzzle.npy")
solutions = np.load("/data/very_easy_solution.npy")
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

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

if __name__ == "__main__":
    print(solve(hard2))
    print(hard2)
