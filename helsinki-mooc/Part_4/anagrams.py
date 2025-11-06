# Write your solution here

def anagrams(string1, string2):
  sorted1 = sorted(string1.lower())
  sorted2 = sorted(string2.lower())
  if sorted1 == sorted2:
    return True
  else:
    return False


if __name__ == "__main__":
  print(anagrams("tame", "meta"))
