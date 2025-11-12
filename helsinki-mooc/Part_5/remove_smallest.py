# Write your solution here

def remove_smallest(numbers: list):
  smallestNum = numbers[0]

  for num in numbers:
    if num < smallestNum:
      smallestNum = num
  numbers = numbers.remove(smallestNum)

if __name__ == "__main__":
  numbers = [2, 4, 6, 1, 3, 5]
  remove_smallest(numbers)
  print(numbers)

#simplier using the min built in method: # O(n)
# def remove_smallest(numbers: list):
#     smallest = min(numbers)
#     numbers.remove(smallest) 
    
