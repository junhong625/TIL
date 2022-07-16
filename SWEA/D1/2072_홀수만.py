T = int(input())
for i in range(1, T+1):
    total = 0
    nums = input().split()
    for j in range(10):
        if int(nums[j]) % 2 == 1:
            total += int(nums[j])
    print('#%d %d' %(i, total))
