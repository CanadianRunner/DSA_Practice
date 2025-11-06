# Write your solution here

newList = [1, 2, 3, 4, 5]

while True:
    newIndex = int(input("Index:" ))
    if newIndex == -1:
      break
    newValue = int(input("New value: "))
    newList[newIndex] = newValue

    print(newList)