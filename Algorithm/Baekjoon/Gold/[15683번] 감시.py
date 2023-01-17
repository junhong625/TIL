import sys

input = sys.stdin.readline

delta = [(0,1),(1,0),(0,-1),(-1,0)]

def cctview(grid, idx=0):
    if idx == len(cctv):        # 모든 cctv의 시야 방향을 정했을 경우
        tot = 0                 # 사각지대 수
        for line in grid:       # 0(=사각지대)의 개수를 모두 더함
            for cert in line:
                if not cert:
                    tot+= 1 
        global minV
        if minV > tot:
            minV = tot
        return
    a, b, cert = cctv[idx]      # a = x좌표, b = y좌표, cert = cctv 종류
    grid[a][b] = 1              # cctv 위치는 사각지대 X
    for i in range(4 if cert != 5 else 1):  # 방향 기준점 설정(4방위를 모두 체크하는 5를 제외하고 나머지는 4방향 체크)
        if cert == 1:           # cctv가 1일 경우
            view = [delta[i]]
        elif cert == 2:         # cctv가 2일 경우
            view = [delta[i],delta[(i+2) % 4]]
        elif cert == 3:         # cctv가 3일 경우
            view = [delta[i],delta[(i+1) % 4]]
        elif cert == 4:         # cctv가 4일 경우
            view = [delta[i],delta[(i+1) % 4],delta[(i+2) % 4]]
        else:                   # cctv가 5일 경우
            view = delta

        stack = []              # 이번 cctv가 없앤 사각지대들
        for dx,dy in view:      # 이번 cctv가 없앨 사각지대를 한 방향씩 조회
            x, y = a+dx, b+dy 
            while 0 <= x < N and 0 <= y < M and grid[x][y] != 6:
                if not grid[x][y]:  # 이번 cctv가 없앤 사각지대일 경우 stack에 추가
                    grid[x][y] = 1
                    stack.append((x,y))
                x += dx
                y += dy
        cctview(grid, idx+1)    # 다음 cctv 조회
        while stack:            # 이번 cctv가 없앤 사각지대들 다시 사각지대로 변경
            x, y = stack.pop()
            grid[x][y] = 0


N, M = map(int, input().split())

office = [list(map(int, input().split())) for _ in range(N)]
cctv = []
minV = float('inf')

for i in range(N):              # cctv들을 cctv리스트에 추가(x좌표, y좌표, cctv종류)
    for j in range(M):
        if 0 < office[i][j] < 6:
            cctv.append((i,j,office[i][j]))

cctview(office[::])
print(minV)