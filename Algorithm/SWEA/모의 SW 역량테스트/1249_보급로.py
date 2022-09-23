import sys, collections

sys.stdin = open('TIL/Algorithm/SWEA/모의 SW 역량테스트/input.txt', 'r')

def spfa(x, y):
    q = collections.deque([[x, y, int(map[x][y])]])
    while q:
        x, y, v = q.popleft()
        for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
            if 0 <= x+dx < N and 0 <= y+dy < N and v + int(map[x+dx][y+dy]) < work_map[x+dx][y+dy]:
                work_map[x+dx][y+dy] = v+int(map[x+dx][y+dy])
                q.append([x+dx, y+dy, v+int(map[x+dx][y+dy])])
    return work_map[N-1][N-1]

T = int(input())

for t in range(1, T+1):
    N = int(input())
    map = [list(input()) for _ in range(N)]
    work_map = [[float('inf') for _ in range(N)] for _ in range(N)]
    print(f'#{t} {spfa(0,0)}')