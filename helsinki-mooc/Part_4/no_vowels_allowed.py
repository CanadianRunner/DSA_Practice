# Write your solution here

def no_vowels(vowels: str):
  newArray = []
  for v in vowels:
    if v != "a" and v != "e" and v != "i" and v != "o" and v != "u":
      newArray.append(v)
  return "".join(newArray)

if __name__ == "__main__":
  my_string = "this is an example"
  print(no_vowels(my_string))


  