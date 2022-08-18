import sys

N, M = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))

start, end = (sum(trees)-M)//N, max(trees) # 지정할 수 있는 최대값으로 지정

while start <= end:
    total = 0
    H = (start+end)//2
    for tree in trees:
        if tree > H:
            total += tree-H
    if total >= M:
        start = H + 1
    else:
        end = H - 1
print(end)