import sys

sys.stdin = open('SWEA/SW Test 샘플문제/input.txt', 'r')

delta = [[0,1], [1,0], [0,-1], [-1,0]]

def check_case(idx, total, cnt):

    if idx == len(cores):
        global maxCores, minV
        if cnt > maxCores or (cnt == maxCores and minV > total):
            maxCores, minV = cnt, total
        return

    i, j = cores[idx]

    for dx, dy in delta:
        if dx == 1:
            for a in range(i+1, N):
                if maxi[a][j] != 0:
                    break
            else:
                for a in range(i+1, N):
                    maxi[a][j] = 2
                check_case(idx+1, total+len(range(i+1, N)), cnt+1)
                for a in range(i+1, N):
                    maxi[a][j] = 0
        elif dx == -1:
            for a in range(0, i):
                if maxi[a][j] != 0:
                    break
            else:
                for a in range(0, i):
                    maxi[a][j] = 2
                check_case(idx+1, total+len(range(0, i)), cnt+1)
                for a in range(0, i):
                    maxi[a][j] = 0
        if dy == 1:
            for b in range(j+1, N):
                if maxi[i][b] != 0:
                    break
            else:
                for b in range(j+1, N):
                    maxi[i][b] = 2
                check_case(idx+1, total+len(range(j+1, N)), cnt+1)
                for b in range(j+1, N):
                    maxi[i][b] = 0
        elif dy == -1:
            for b in range(0, j):
                if maxi[i][b] != 0:
                    break
            else:
                for b in range(0, j):
                    maxi[i][b] = 2
                check_case(idx+1, total+len(range(0, j)), cnt+1)
                for b in range(0, j):
                    maxi[i][b] = 0
    check_case(idx+1, total, cnt)

T = int(input())

for t in range(1, T+1):
    N = int(input())
    maxi = [list(map(int, input().split())) for _ in range(N)]

    cores = []

    for i in range(N):
        for j in range(N):
            if maxi[i][j] == 1 and i not in (0, N-1) and j not in (0, N-1):
                cores.append([i,j])

    maxCores, minV = 0, N**2
    check_case(0, 0, 0)
    print(f'#{t} {minV}')