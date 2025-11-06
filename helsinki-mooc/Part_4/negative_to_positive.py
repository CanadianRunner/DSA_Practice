# Write your solution here

userInput = int(input("Please type in a positive integer: "))

for i in range(-userInput, userInput+1):
  if i == 0:
    continue
  print(i)