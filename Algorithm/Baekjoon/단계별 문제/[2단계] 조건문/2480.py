nums = list(map(int,input().split()))
nums_count = {}
for num in nums:
    if num in nums_count:
        nums_count[num] += 1
    else:
        nums_count[num] = 1
max_num = max(nums_count, key=lambda x:nums_count[x])
if nums_count[max_num] == 3:
    print(10000+max_num*1000)
elif nums_count[max_num] == 2:
    print(1000+max_num*100)
else:
    print(max(nums)*100)