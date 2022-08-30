import sys

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    nums.append(list(map(int, sys.stdin.readline().split())))

for i in sorted(nums, key=lambda x:(x[1], x[0])):
    print(*i)