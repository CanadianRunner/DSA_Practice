def longest_series_of_neighbours(nums):
    if not nums:
        return 0

    best = 1
    curr = 1
    i = 0
    while i < len(nums) - 1:
        left = nums[i]
        right = nums[i + 1]
        if left == right:
          best += 1
        

        if abs(left - right) == 1:
            curr += 1
            if curr > best:
                best = curr
        else:
            curr = 1

        i += 1

    return best


if __name__ == "__main__":
  my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
  print(longest_series_of_neighbours(my_list))