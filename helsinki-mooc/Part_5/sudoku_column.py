# Write your solution here

# Goal:
#   Check a single column of a 9x9 Sudoku grid.
#   Return True if the column contains numbers 1–9 at most once (zeros are ignored).

def column_correct(sudoku: list, column_no: int):
    matched_nums = []
    for r in range(len(sudoku)):
        item = sudoku[r][column_no]
        if item == 0:
            continue
        if item in matched_nums:
            return False
        matched_nums.append(item)
    return True

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(column_correct(sudoku, 0))  # False
    print(column_correct(sudoku, 1))  # True
