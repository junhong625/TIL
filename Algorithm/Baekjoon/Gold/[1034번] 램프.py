# 문제: 켜져 있는 행의 최댓값 구하기

# 조건: 1) 0 < N, M <= 50
#      2) 램프는 꺼져있거나(0) 켜져있거나(1)
#      3) 스위치를 누르는 횟수 K, 0 <= K <= 1000

# 방법: 1) 행에서 꺼져있는 램프(0)의 개수가 K보다 작거나같고 홀, 짝이 맞다면 행의 모든 램프를 켤 수 있다.
#      2) 행의 모든 램프를 켤 수 있다면 해당 행과 똑같이 생긴 행들을 찾는다면 최대값을 구할 수 있다. 

def find_zero(row): # 꺼져있는 램프 개수 찾기
    cnt = 0
    for n in row:
        if n == "0":
            cnt += 1
    return cnt

def find_same_row(idx): # 같은 행 개수 찾기
    global checked
    cnt = 1
    row1 = grid[idx]
    checked[idx] = idx
    for i, row2 in enumerate(grid[idx+1:]):
        if row1 == row2:
            cnt += 1
            checked[idx+1+i] = idx
    return cnt

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [input().rstrip() for _ in range(N)]
K = int(input())

max_cnt = 0
checked = [-1 for _ in range(N)]

for i in range(N):
    if checked[i] >= 0 :
        continue
    row = grid[i]
    cnt = find_zero(row)
    if K >= cnt and K % 2 == cnt % 2: # 방법 1
        max_cnt = max(max_cnt, find_same_row(i)) # 방법 2

print(max_cnt)
