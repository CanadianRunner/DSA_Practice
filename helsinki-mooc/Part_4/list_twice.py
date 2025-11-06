# Write your solution here

unsortedList = []
sortedList = []

while True:
  userInput = int(input("New item: "))
  if userInput == 0:
    print("Bye!")
    break
  unsortedList.append(userInput)
  sortedList = sorted(unsortedList)
  print(f"The list now: {unsortedList}")
  print(f"The list in order: {sortedList}")
