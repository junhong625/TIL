# 시간 초과

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]


for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    total = 0
    for i in range(x1-1, x2):
        total += sum(grid[i][y1-1:y2])
    print(total)