# 문제: 상점에서 사야하는 물병의 최솟값 구하기

# 조건: 1) 1 <= N <= 10^7
#      2) 1 <= K <= 1000
#      3) 정답이 없을 경우 -1

# 방법: 1) 물병이 홀수일 경우 물병을 하나 빼고 남은 물병들 합치기
#      2) bottles에 들어있는 물병의 수가 K와 같아질 때까지 첫번째 물병과 두번째 물병을 더하는 과정을 반복(상점에서 물병 구매)

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

bottles = deque()
cur = 1
res = 0

# 방법 1
while N:
    if N % 2:
        bottles.append(cur)
    N = N // 2
    cur *= 2

# 방법 2
while len(bottles) > K:
    v1, v2 = bottles.popleft(), bottles.popleft()
    res += v2 - v1
    bottles.appendleft(v2*2)
print(res)