import sys

input = sys.stdin.readline

N, M = map(int, input().split())
square = [input().rstrip() for _ in range(N)]
maxV = 0

for i in range(N):
    for j in range(M):
        w = maxV
        while True:
            if i+w >= N or j+w >= M:
                break
            if square[i][j] == square[i+w][j] == square[i][j+w] == square[i+w][j+w]:
                maxV = max(maxV, w+1)
            w += 1
print(maxV ** 2)