# Write your solution here

def create_tuple(x: int, y: int, z: int):
  values = [x, y, z]
  sortedValues = sorted(values)
  smallest = sortedValues[0]
  largest = sortedValues[2]
  valuesSum = sum(values)

  tupleValues = (smallest, largest, valuesSum)

  return tupleValues

#simplified verison utilizing min/max

# def create_tuple(x: int, y: int, z: int):
#   return (min(x, y, z), max(x, y, z), x+y+z)

if __name__ == "__main__":
  print(create_tuple(5, 3, -1))