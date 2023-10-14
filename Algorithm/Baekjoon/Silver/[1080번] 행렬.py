# 문제: 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값 구하기

# 조건: 1) 1 <= N, M <= 50
#      2) 행렬을 뒤집을 때는 3X3 행렬을 뒤집는다("0" -> "1" or "1" -> "0")
#      3) 행렬 A를 행렬 B로 바꿀 수 없을 경우 -1 출력

# 방법: 그리디 방식으로 풀이
#      1) 3X3 행렬을 뒤집기에 N-2, M-2를 하여 순회
#      2) 해당 위치의 행렬 A의 원소가 행렬 B의 원소와 같지 않을 경우 3X3 행렬 뒤집기 실행(뒤집으면서 cnt + 1)
#      3) 모두 순회를 마친 후 행렬 A와 행렬 B가 같지 않을 경우 -1 출력, 같을 경우 뒤집은 횟수 실행


import sys

def reverse(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            grid2[i][j] = "1" if grid2[i][j] == "0" else "0"

input = sys.stdin.readline

N, M = map(int, input().split())

grid1 = [list(map(str, input().rstrip())) for _ in range(N)]
grid2 = [list(map(str, input().rstrip())) for _ in range(N)]
cnt = 0

for i in range(N-2): # 방법 1
    for j in range(M-2): # 방법 1
        if grid1[i][j] != grid2[i][j]: # 방법 2
            reverse(i, j)
            cnt += 1

for n in range(N):
    if grid1[n] != grid2[n]:
        print(-1)
        exit()

print(cnt)