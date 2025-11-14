# Write your solution here

def histogram(string: str):
  letterCount = {}
  i = 1
  for char in string:
    if char not in letterCount:
      letterCount[char] = 0
    letterCount[char] +=1

  for key, value in letterCount.items():
    print(f"{key} {value*"*"}")

if __name__ == "__main__":
  histogram("statistically")
