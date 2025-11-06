# Write your solution here

def list_of_stars(nums):
  for count in nums:
    print("*" * count)


if __name__ == "__main__":
  nums = [3, 7, 1, 1, 2]
  list_of_stars(nums)
