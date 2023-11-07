# 문제: 소용돌이 예쁘게 출력하기

# 조건: 1) -5000 <= r1, c1, r2, c2 <= 5000
#      2) 0 ≤ r2 - r1 ≤ 49
#      3) 0 ≤ c2 - c1 ≤ 4

# 방법: 1) 각 좌표를 순회하면서 각 좌표의 값 구하기
#      2) 각 조건에 따른 가중치 규칙에 따라 좌표의 값을 찾아 grid에 집어넣기
#      3) 최대길이 수에 맞춰 공백을 출력하며 예쁘게 출력하기


import sys

input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())

grid = [[1 for _ in range(c2-c1+1)]for _ in range(r2-r1+1)]
maxV = 0

# 방법 2
def value(x, y):
    v, w, z = 1, 0, 0
    if abs(x) >= abs(y):
        if x < 0:
            w += 3
            z = 1 if y < 0 else -1
        else:
            w += 7
            z = 1 if y > 0 else -1
        for _ in range(abs(x)):
            v += w
            w += 8
        for _ in range(abs(y)):
            v += z
    else:
        if y < 0:
            w += 5
            z = 1 if x > 0 else -1
        else:
            w += 1
            z = 1 if x < 0 else -1
        for _ in range(abs(y)):
            v += w
            w += 8
        for _ in range(abs(x)):
            v += z
    global maxV
    maxV = max(maxV, v)
    return v

# 방법 1
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        grid[i-r1][j-c1] = value(i, j)

# 방법 3
maxL = len(str(maxV))
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        for _ in range(maxL - len(str(grid[i][j]))):
            print(" ", end="")
        print(grid[i][j], end=" ")
    print()