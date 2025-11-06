# Write your solution here

def all_the_longest(my_list):
  result = []
  newArray = max(my_list, key=len)

  for word in my_list:
    if len(word) == len(newArray):
      result.append(word)
  return result

if __name__ == "__main__":
  my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
  result = all_the_longest(my_list)
  print(result) # ['dorothy', 'richard']