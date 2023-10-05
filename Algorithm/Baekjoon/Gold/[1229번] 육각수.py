# 문제: N을 만들기 위해 필요한 육각수 개수 최소값 구하기
# 시간 제한 2초 / 메모리 제한 128MB

# 조건: 1) 1 <= N <= 1000000

# 방법: 1) 사전에 주어진 정보 dp에 넣어두기
#      2) dp에 육각수들은 1개로 바로 최소값 계산이 가능하니 넣어두기 
#      3) 13부터 N까지 순회하고 N 이하의 육각수들을 이중 순회하며 dp[N-육각수]에서 최소값을 게산해 N의 최소값 계산
#      4) N이 육각수에 해당할 경우 바로 출력

import sys

input = sys.stdin.readline

N = int(input())

hexagonal_numbers = []

num = 1
std = 1
dp = [0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 2] + [0 for _ in range(N-12)] # 방법 2

# 육각수 구하기
while num <= N:
    dp[num] = 1 # 방법 2
    hexagonal_numbers.append(num)
    std += 1
    num = std * (2 * std - 1)

# 최소값 찾기
def find_min(N): # 방법 3
    global dp

    minV = float('inf')

    for hn in hexagonal_numbers:
        if N < hn:
            break
        minV = min(minV, dp[N-hn])
    dp[N] = minV + 1

if dp[N]: # 방법 4
    print(dp[N])
    exit()

for i in range(13, N+1):
    if not dp[i]: # N 이하의 육각수들 계산 생략
        find_min(i)

# print(dp)
print(dp[-1])