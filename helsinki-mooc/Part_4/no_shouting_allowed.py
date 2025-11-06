# Write your solution here

def no_shouting(list_strings: list):
  new_string = []
  for item in list_strings:
    if not item.isupper():
      new_string.append(item)
  return new_string
    

if __name__ == "__main__":
  my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
  pruned_list = no_shouting(my_list)
  print(pruned_list)