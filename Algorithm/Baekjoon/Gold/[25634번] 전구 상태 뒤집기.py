# 문제: 켜져 있는 전구의 밝기 최댓값 구하기

# 조건: 1) 1 <= N <= 200000
#      2) 전구는 꺼져있거나(0) 켜져있거나(1)
#      3) 1 <= 전구의 밝기 <= 5000
#      4) 연속한 전구를 한 개 이상 선택해서 뒤집을 수 있는데 딱 한번만 가능

# 방법: 1) 누적합 방식을 통해서 최대갑 구하기
#      2) 누적된 값이 음수가 되면 0으로 초기화
#      3) maxB가 0일 경우 모든 전구를 안 뒤집는 것이 최대값이기에 가장 작은 값을 뒤집어서 조건 충족
#      4) maxB가 존재할 경우 기존의 값에서 maxB를 더해 최대 밝기 구하기


import sys

input = sys.stdin.readline

N = int(input())
bulbs = list(map(int, input().split()))
on_off = list(map(int, input().split()))
tot = sum([bulbs[i] for i in range(N) if on_off[i]])

ans = 0
maxB = 0
# 방법 1
for i in range(N):
    if not on_off[i]:
        ans += bulbs[i]
    else:
        ans -= bulbs[i]
    # 방법 2
    if ans < 0:
        ans = 0
    maxB = max(maxB, ans)

# 방법 3
if maxB == 0:
    print(tot - min(bulbs))
# 방법 4
else:
    print(tot + maxB)
