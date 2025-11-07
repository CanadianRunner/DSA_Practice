# Write your solution here

# Goals:
#   Start at (row_no, column_no) which is the top-left of a 3x3 block.
#   Walk a 3 by 3 window to the right and down from that start.
#   Ignore zeros since those are blanks.
#   Track which non-zero numbers I have already seen.
#   Return False on the first duplicate, otherwise True.

def block_correct(sudoku: list, row_no: int, column_no: int):
    seen = set()
    for r in range(row_no, row_no + 3):
        for c in range(column_no, column_no + 3):
            value = sudoku[r][c]
            if value == 0:
                continue
            if value in seen:
                return False
            seen.add(value)
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

  print(block_correct(sudoku, 0, 0)) #False
  print(block_correct(sudoku, 1, 2)) #True