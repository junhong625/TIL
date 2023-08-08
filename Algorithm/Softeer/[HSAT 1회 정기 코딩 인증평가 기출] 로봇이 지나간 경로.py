import sys
from collections import deque 

def check(x, y):
    cnt = 0
    for idx, (dx, dy) in enumerate(direction):
        dx += x
        dy += y
        if 0 <= dx < H and 0 <= dy < W and grid[dx][dy] == '#':
            start = idx
            cnt += 1
            if cnt > 1:
                return 5
    return start

def find_path(x, y, d):
    path = ""
    q = deque()
    q.append([x, y, d])

    while q:
        x, y, d = map(int, q.popleft())
        print(x, y, arrow[d])
        for i in range(4):
            dx = x + direction[i][0]
            dy = y + direction[i][1]
            if 0 <= dx < H and 0 <= dy < W and grid[dx][dy] == '#':
                print(i)
                if i == d:
                    q.append([dx+direction[i][0], dy+direction[i][1], i])
                    path += "A"
                    break
                elif i == d-1 or i == d-1+4:
                    q.append([dx+direction[i][0], dy+direction[i][1], i])
                    path += "LA"
                    break
                elif i == (d+1)%4:
                    q.append([dx+direction[i][0], dy+direction[i][1], i])
                    path += "RA"
                    break
    
    return path

input = sys.stdin.readline

H, W = map(int, input().split())

grid = []

for _ in range(H):
    grid.append(input().rstrip())

minV, x, y = float('inf'), 0 ,0

direction = [(0,1), (1,0), (0,-1), (-1,0)]
arrow = ['>', 'v', '<', '^']

for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            d = check(i,j)
            print(i+1, j+1)
            print(arrow[d])
            if d != 5:
                print(find_path(i, j, d))
                sys.exit()