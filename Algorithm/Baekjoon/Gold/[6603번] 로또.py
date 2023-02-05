import sys
from itertools import combinations

input = sys.stdin.readline

N = 1

## combinations 사용
# while N:
#     N, *nums = map(int, input().split())
#     if N == 0:
#         break
#     comb = sorted(list(combinations(nums, 6)))
#     for case in comb:
#         print(*case)
#     print()

## combinations 미사용
def comb(idx=-1, case=[]):
    if len(case) == 6:
        print(*case)
        return

    for i in range(idx+1, len(nums)):
        comb(i, case+[nums[i]])

while N:
    N, *nums = map(int, input().split())
    if not N:
        break
    comb()
    print()