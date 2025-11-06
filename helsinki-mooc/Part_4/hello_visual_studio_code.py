# Write your solution here

while True:
  userInput = input("Editor: ")
  x = userInput.strip().lower()
  if x == "visual studio code":
    print("an excellent choice!")
    break
  elif x in ("word", "notepad"):
    print("awful")
  else:
    print("not good")
