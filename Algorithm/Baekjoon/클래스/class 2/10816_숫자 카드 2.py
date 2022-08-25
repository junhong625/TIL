import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
find_num = list(map(int, sys.stdin.readline().split()))

nums_dict = {}

for n in cards: # counting sort
    if n in nums_dict: 
        nums_dict[n] += 1
    else:
        nums_dict[n] = 1

for m in find_num:
    if m in nums_dict:
        print(nums_dict[m], end=' ')
    else:
        print(0, end=' ')