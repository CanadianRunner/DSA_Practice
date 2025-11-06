# Write your solution here
def list_sum(a, b):
  newList = []
  i = 0
  while i < len(a):
    sumOfArrays = a[i]+ b[i]
    newList.append(sumOfArrays)
    i +=1
  return newList

if __name__ == "__main__":
  a = [1, 2, 3]
  b = [7,8, 9]
  print(list_sum(a, b))