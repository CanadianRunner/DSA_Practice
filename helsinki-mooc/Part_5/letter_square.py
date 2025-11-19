# Write your solution here

layers = int(input("Layers: "))

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

size = 2 * layers - 1

for r in range(size):
    row_text = ""
    for c in range(size):
        dist_from_edge = min(r, c, size - 1 - r, size - 1 - c)

        letter_index = layers - 1 - dist_from_edge
        letter = letters[letter_index]

        row_text += letter
    print(row_text)
