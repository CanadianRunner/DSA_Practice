# write your solution here

def largest():
  with open("numbers.txt") as numberText:
    numbers = []
    for line in numberText:
        number = int(line.strip())
        numbers.append(number)
    
    return max(numbers)

if __name__ == "__main__":
  print(largest())
