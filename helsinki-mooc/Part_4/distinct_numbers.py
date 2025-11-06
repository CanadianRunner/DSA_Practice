# Write your solution here

def distinct_numbers(my_list):
  sortedList = sorted(my_list)
  result = []
  
  for n in sortedList:
    if not result or n != result[-1]:
      result.append(n)
  return result


if __name__ == "__main__":
  my_list = [3, 2, 2, 1, 3, 3, 1]
  print(distinct_numbers(my_list))