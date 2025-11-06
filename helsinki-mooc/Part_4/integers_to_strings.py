# Write your solution here
def formatted(my_list):
  out = []
  for items in my_list:
    out.append(f"{items:.2f}")
  return out
    


if __name__ == "__main__":
  my_list = [1.234, 0.3333, 0.11111, 3.446]
  new_list = formatted(my_list)
  print(new_list)