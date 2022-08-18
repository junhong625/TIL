# 이분탐색 활용

import sys

K, N = map(int, sys.stdin.readline().split())

num_list = [int(sys.stdin.readline()) for _ in range(K)]

start, end = 1, max(num_list) # 최소값 : 1, 최대값 : 랜선 중 최대 길이 

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for num in num_list:
        cnt += num // mid
    if cnt >= N:        # cnt > N 을 할 경우 cnt와 N이 같은 값일 경우 end가 mid값으로 변경되며 최대값을 구해야하는 문제 조건에 어긋나게 된다.
        start = mid + 1 # 따라서 최소값을 구해야 할 경우에 cnt > N 을 하고 최대값을 구해야 하는 경우에는 cnt >= N 을 하는 것이 알맞다.
    else:
        end = mid - 1

print(end)