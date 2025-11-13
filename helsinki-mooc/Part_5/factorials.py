# Write your solution here

def factorials(n: int):
  result = {}
  i = 1
  current_factorial = 1

  while i <= n:
    current_factorial *= i
    result[i] = current_factorial
    i+=1
  
  return result


if __name__ == "__main__":
  k = factorials(5)
  print(k[1])
  print(k[3])
  print(k[5])
  