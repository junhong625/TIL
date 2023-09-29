# 문제: 목표 홍보 인원을 달성할 수 있는 최소 비용 구하기
# 시간 제한 2초 / 메모리 제한 128MB

# 조건: 1) 0 <= C <= 1000 | 목표 홍보 인원
#      2) 0 <= N <= 20 | 도시의 수
#      3) 0 <= V <= 100 | 한 번의 홍보를 통해 얻을 수 있는 고객 수

# 방법: 1) DP + 배낭

import sys

input = sys.stdin.readline

C, N = map(int, input().split())

cost_list = [list(map(int, input().split())) for _ in range(N)]
dp = [float('inf') for _ in range(C+100)]
dp[0] = 0

# 방법 1
for cost, num_people in cost_list:
    for i in range(num_people, C+100):
        dp[i] = min(dp[i-num_people]+cost, dp[i])

print(min(dp[C:]))