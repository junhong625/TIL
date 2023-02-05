import sys
from itertools import combinations
import pprint

input = sys.stdin.readline

N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]


case = list(combinations(range(1,N+1), 2)) + [(i, i) for i in range(1, N+1)]

minV = 9999999999

while case:
    d1, d2 = case.pop()
    
    # 기준점 선정
    for x in range(N):
        for y in range(N):
            flag = True
            while True:
                if 0 <= x < x + d1 + d2 < N and 0 <= y-d1 < y < y+d2 < N:
                    score = [0] * 5
                    show_grid = [[0]*N for _ in range(N)]
                    # 경계선 나누기
                    for v in range(d1+1):
                        show_grid[x+v][y-v] = 5 # 1번 
                        show_grid[x+d2+v][y+d2-v] = 5 # 4번
                    for v in range(d2+1):
                        show_grid[x+v][y+v] = 5 # 2번
                        show_grid[x+d1+v][y-d1+v] = 5 # 3번
                    
                    # 경계선 기준으로 각 선거구 인원 더하기
                    for r in range(N):
                        for c in range(N):
                            if 0 <= r < x+d1 and 0 <= c <= y and not show_grid[r][c] == 5:
                                score[0] += grid[r][c]
                                show_grid[r][c] = 1
                            elif 0 <= r <= x+d2 and y < c < N and not show_grid[r][c] == 5:
                                score[1] += grid[r][c]
                                show_grid[r][c] = 2
                            elif x+d1 <= r < N and 0 <= c < y-d1+d2 and not show_grid[r][c] == 5:
                                score[2] += grid[r][c]
                                show_grid[r][c] = 3
                            elif x+d2 < r < N and y-d1+d2 <= c < N and not show_grid[r][c] == 5:
                                score[3] += grid[r][c]
                                show_grid[r][c] = 4
                            else:
                                score[4] += grid[r][c]
                                for i in range(c+1, N):
                                    if show_grid[r][i] == 5:
                                        for j in range(c+1, i):
                                            show_grid[r][j] = 5
                    # pprint.pprint(show_grid)
                    minV = min(minV, max(score)-min(score))
                if flag and d1 != d2:
                    d1, d2 = d2, d1
                    flag = False
                    continue
                else:
                    break
                    

print(minV)