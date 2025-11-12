# Write your solution here

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


def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number


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
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print("")
    print("Three numbers added:")
    print("")
    print_sudoku(sudoku)