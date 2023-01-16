import sys
from itertools import permutations

input = sys.stdin.readline

chars = input().rstrip()

num = ""
nums = []

for c in chars:
    if c.isdigit():
        num += c
    else:
        nums.append(int(num))
        num = c

nums.append(int(num))

print(list(permutations(range(len(nums)), 3)))

55 - 50 + 40 + 100 - 50 

