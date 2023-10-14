# 문제: N^3 개수의 주사위를 쌓아 만든 정육면체를 탁자위에 올려 노출된 5개면의 최소합 구하기

# 조건: 1) 1 <= N <= 1000000
#      2) 1 <= 주사위 한 면의 값 <= 50

# 방법: 1) 1개의 면만 노출되는 주사위 개수 구하고 주사위 최소값 곱하기
#      2) 2개의 면이 노출되는 주사위 개수 구하기
#      3) 붙어있는 2면의 최소값 구하기
#      4) 3개의 면이 노출되는 주사위 개수 구하기
#      5) 붙어있는 3면의 최소값 구하기
#      6) N이 1일 경우 예외처리로 바로 출력

import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
dice = list(map(int, input().split()))
min2, min3 = float('inf'), float('inf')
ex2 = [(0,5), (5,0), (1,4), (4,1), (3,2), (2,3)]
ex3 = [(0,1,4), (0,1,5), (1,4,5), (0,4,5), (0,2,3), (0,2,5), (2,3,5), (0,3,5), (1,2,3), (1,2,4), (2,3,4), (1,3,4)]

# 방법 6
if N == 1: 
    print(sum(dice) - max(dice))
    exit()

# 방법 3
for a, b in list(combinations(range(6), 2)):
    if (a, b) in ex2:
        continue
    min2 = min(min2, dice[a]+dice[b])

# 방법 5
for a, b, c in list(combinations(range(6), 3)):
    if (a,b,c) in ex3:
        continue
    min3 = min(min3, dice[a]+dice[b]+dice[c])

# 방법 1
ans1 = ((N-2) * (N-2) * 5 + (N-2) * 4) * min(dice)
# 방법 2 * 방법 3
ans2 = ((N-2) * 4 + (N-1) * 4) * min2
# 방법 4 * 방법 5
ans3 = 4 * min3
print(ans1 + ans2 + ans3)