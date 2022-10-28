def centered_average(nums):
  trim = sorted(nums)[1:-1]
  return int(sum(trim) / len(trim))





nums = [-10,-4,-2,-4,-2,0]
print(centered_average(nums))
