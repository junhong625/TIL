A = int(input())
B = int(input())
C = int(input())
nums = {str(x):0 for x in range(10)}
result = A * B * C
for num in str(result):
    nums[num] += 1
for num in nums.values():
    print(num)
