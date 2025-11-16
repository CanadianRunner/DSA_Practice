# Write your solution here

phoneBook = {}

while True:
  userInputStart = input("1 search, 2 add, 3 quit:")
  if userInputStart == "3":
    print("quitting...")
    break

  elif userInputStart == "2":
    inputName = input("name: ")
    inputNumber = input("number: ")
    if inputName not in phoneBook:
      phoneBook[inputName] = []
    phoneBook[inputName].append(inputNumber)
    print("ok!")

  elif userInputStart == "1":
    inputName = input("name: ")
    if inputName in phoneBook:
      for number in phoneBook[inputName]:
        print(number)
    else:
      print("no number")
  else:
    pass
