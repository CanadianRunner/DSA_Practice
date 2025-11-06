# Write your solution here

wordList = []

while True:
  userInput = input("Word: ")

  if userInput in wordList:
    print(f"You typed in {len(wordList)} different words")
    break

  wordList.append(userInput)
  
