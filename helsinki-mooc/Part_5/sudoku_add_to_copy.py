# Write your solution here

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    grid_copy = [row[:] for row in sudoku]
    grid_copy[row_no][column_no] = number
    return grid_copy


def print_sudoku(sudoku: list):
    total_rows = len(sudoku)
    total_cols = len(sudoku[0]) if total_rows > 0 else 0

    for r in range(total_rows):
        for c in range(total_cols):
            value = sudoku[r][c]
            if value == 0:
                cell_text = "_"
            else:
                cell_text = str(value)

            print(cell_text, end=" ")

            if c == 2 or c == 5:
                print(" ", end="")

        print("")

        if r == 2 or r == 5:
            print("")

if __name__ == "__main__":
  sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
  ]

  grid_copy = copy_and_add(sudoku, 0, 0, 2)
  print("Original:")
  print_sudoku(sudoku)
  print()
  print("Copy:")
  print_sudoku(grid_copy)
  