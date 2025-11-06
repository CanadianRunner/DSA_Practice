# Write your solution here
def most_common_character(string: str):
  bestChar = None
  bestCount = 0
  counts = {}

  for char in string:
    counts[char] = counts.get(char, 0)+1
    if counts[char] > bestCount:
      bestCount = counts[char]
      bestChar = char
      
  return bestChar


if __name__ == "__main__":
  first_string = "abcdbde"
  print(most_common_character(first_string))

  second_string = "exemplaryelementary"
  print(most_common_character(second_string))