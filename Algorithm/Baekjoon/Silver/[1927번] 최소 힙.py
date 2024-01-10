# 문제: 최소 힙을 이용한 연산 프로그램 작성

# 조건: 1) 1 <= N <= 100,000
#      2) X == 0 : 제일 작은 값 출력후 배열에서 제거
#      2-1) 배열이 비었을 경우 0 출력
#      3) X > 0 : 배열에 추가

# 풀이: heapq 라이브러리 이용

# 방법: 1) 0이면 배열에서 pop한 값을 출력하거나 0을 출력
#      2) 자연수면 배열에 추가

import sys, heapq

input = sys.stdin.readline

N = int(input())
H = []

for _ in range(N):
    X = int(input())
    if X:
        heapq.heappush(H, X)
    else:
        print(heapq.heappop(H) if len(H) else 0)