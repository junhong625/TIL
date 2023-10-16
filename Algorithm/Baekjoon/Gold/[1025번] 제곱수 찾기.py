# 문제: 행렬에서 행과 열이 각각 등차수열을 이루는 위치의 원소들을 모아 만든 정수들 중 최대 완전제곱수 구하기

# 조건: 1) 1 <= N, M <= 9
#      2) 0 <= 행렬 원소  <= 9
#      3) 완전 제곱수를 만들 수 없는 경우 -1 출력

# 방법: 1) 4중 반복문을 통해 등차수열을 적용한 원소를 더해서 정수 구하기
#      2) 만들어지는 정수마다 제곱근을 하여 1로 나누었을 때 나머지가 없으면 완전 제곱수인지 확인
#      3) 정수가 완전 제곱수일 경우 max와 비교하여 더 큰 값을 maxV로 설정

import sys
from math import sqrt

input = sys.stdin.readline

N, M = map(int, input().split())

nums = [input().rstrip() for _ in range(N)]

res = -1

# 방법 1
for i in range(N):
    for j in range(M):
        for a in range(-N+1, N):
            for b in range(-M+1, M):
                num = ''
                x, y = i, j
                while 0 <= x < N and 0 <= y < M:
                    num += nums[x][y]
                    if a == 0 and b == 0:
                        break
                    # 방법 2
                    if not sqrt(int(num)) % 1:
                        # 방법 3
                        res = max(int(num), res)
                    x += a
                    y += b
                    print(num)

print(res)

