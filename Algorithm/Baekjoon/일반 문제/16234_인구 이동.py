import sys

input = sys.stdin.readline

N, L, R = map(int, input().split())

maps = []
border = []

for i in range(N):
    maps.append(list(map(int, input().split())))
    border.append([[i, j] for j in range(N)])

delta = [[0, 1], [1, 0]]

def bfs(x, y):
    for dx, dy in delta:
        dx += x
        dy += y
        if 0 <= dx < N and 0 <= dy < N:
            if L <= abs(maps[x][y] - maps[dx][dy]) <= R:

print(maps)
print(border)
