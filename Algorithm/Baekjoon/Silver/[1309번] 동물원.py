# 문제: 2 x N의 우리에 사자를 배치할 수 있는 경우의 수 

# 조건: 1) 1 <= N <= 10,0000
#      2) 경우의 수는 9901로 나눠야 함

# 풀이: DP 풀이

# 방법: 1) 우리가 없을 때 1, 우리가 2 x 1일 경우 3, 우리가 2 x 2일 경우 7
#      2) 그림을 그리면서 점화식을 그려볼 경우 N이 3인 경우 "마지막 층에 사자가 없는 경우"마다 3가지의 경우의 수가 가능하고, 
#           이 경우를 제외하고는 인접한 사자가 위치한 경우는 있어선 안된다는 조건으로 인해 2가지의 경우의 수가 가능하다.
#      2-1) 마지막 층에 사자가 없는 경우 = dp[N-2]의 경우의 수들
#      2-2) 2-1을 제외한 경우는 dp[N-1] - dp[N-2]
#      3) 즉, dp[N] = dp[N-2] * 3 + (dp[N-1] - dp[N-2]) * 2 와 같은 점화식이 나온다.
#      4) 3을 간단하게 정리하면 dp[N] = dp[N-1] * 2 + dp[N-2] 와 같이 정리된다.
#      5) 메모리를 아끼기 위해 배열이 아닌 변수 두개를 통해 dp 점화식을 실행

import sys

input = sys.stdin.readline

N = int(input())
dp1, dp2 = 1, 3

for i in range(N-1):
    dp1, dp2 = dp2, (dp1+dp2*2)%9901

print(dp2)