# Write your solution here

numberOfItems = int(input("How many items: "))
counter = 0
itemCounter = 1
arrayValues = []

while numberOfItems > counter:
  itemValue = int(input(f"Item{itemCounter}: "))
  counter += 1
  itemCounter += 1
  arrayValues.append(itemValue)

print(arrayValues)

