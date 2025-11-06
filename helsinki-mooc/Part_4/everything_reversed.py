# Write your solution here
def everything_reversed(my_list):
  out = []
  for items in my_list[::-1]:
    out.append(items[::-1])
  return out


if __name__ == "__main__":
  my_list = ["Hi", "there", "example", "one more"]
  new_list = everything_reversed(my_list)
  print(new_list)