# Write your solution here

def times_ten(start_index: int, end_index: int):
  newDict = {}

  while start_index <= end_index:
    timesTen = start_index*10
    newDict[start_index] = timesTen
    start_index += 1
  return newDict

if __name__ == "__main__":
  d = times_ten(3, 6)
  print(d)