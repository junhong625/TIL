import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
N = int(sys.stdin.readline())
nums2 = list(map(int, sys.stdin.readline().split()))
print(nums)

for num in nums2:
    start, end = 0, len(nums)-1
    while start <= end:
        idx = (start+end)//2
        if num > nums[idx]:
            start = idx + 1
        elif num < nums[idx]:
            end = idx - 1
        else:
            break
    if nums[idx] == num:
        print(1)
    else:
        print(0)