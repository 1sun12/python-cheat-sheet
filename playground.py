nums = [1,2,3,4,5,9,6,7,8,5]

for i in nums:
    print(i, end="")

l, r = 0, len(nums) - 1
while l < r:
  nums[l], nums[r] = nums[r], nums[l]
  l += 1
  r -= 1

for i in nums:
    print(i, end="")
