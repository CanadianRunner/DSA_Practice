# Write your solution here

list = []
addedNum = 0

print(f"The list is now {list}")
userInput = ""
while userInput is not "x":
  userInput = input("a(d)d, (r)emove or e(x)it:")
  if userInput == "d":
    addedNum += 1
    list.append(addedNum)
    print(f"The list is now {list}")
  elif userInput == "r":
    list.pop(-1)
    print(f"The list is now {list}")
    addedNum -=1
  elif userInput == "x":
    print("Bye!")
    break
