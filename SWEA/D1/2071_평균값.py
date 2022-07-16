T = int(input())
for i in range(1, T+1):
    total = 0
    nums = input().split()
    for j in range(10):
        total += int(nums[j])
    if total % 10 >= 5:
        print('#%d %d' %(i, total//10+1))
    else:
        print('#%d %d' %(i, total//10))
