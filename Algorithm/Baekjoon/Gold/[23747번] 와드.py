import sys

input = sys.stdin.readline

## bfs를 통해 와드를 찍은 영역 모두 시야에 보이는 것으로 변경
def set_grid(x, y):
    q = [(x,y)]
    visited[x][y] = '.'
    target = grid[x][y]
    while q:
        x, y = q.pop()
        for dx,dy in delta:
            dx += x
            dy += y
            if 0 <= dx < R and 0 <= dy < C and grid[dx][dy] == target and visited[dx][dy] != '.':
                q.append((dx,dy))
                visited[dx][dy] = '.'

## 한별이가 보이는 시야를 모두 탐색
def check_view(x, y):
    direction = {'L':(0,-1), 'R':(0,1), 'U':(-1,0), 'D':(1,0)}
    for i in range(len(move)):
        if move[i] == 'W':
            if visited[x][y] != '.':
                set_grid(x, y)
        else:
            dx, dy = direction[move[i]]
            x += dx
            y += dy
    for dx,dy in delta+[(0,0)]:
        dx += x
        dy += y
        if 0 <= dx < R and 0 <= dy < C:
            visited[dx][dy] = '.'

R, C = map(int ,input().split())

grid = [input().rstrip() for _ in range(R)]
visited = [['#']*C for _ in range(R)]
delta = [(0,1),(0,-1),(1,0),(-1,0)]

x, y = map(int, input().split())

move = list(input().rstrip())

check_view(x-1, y-1)

for view in visited:
    print(*view, sep='')