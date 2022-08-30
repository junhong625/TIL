import sys

N = int(sys.stdin.readline())
nums = {}

for _ in range(N):
    num =int(sys.stdin.readline()) 
    if num in nums:
        nums[num] += 1
    else:
        nums[num] = 1

for key in sorted(nums):
    for _ in range(nums[key]):
        print(key)