# 조건: 가장 많은 고층 빌딩이 보이는 빌딩에서 보이는 빌딩의 수를 출력
# 고려사항: 1) 선분을 그려서 다른 빌딩을 지나거나 접하지 않아야 한다.
# 방법: 기울기를 이용해 왼쪽 방향과 오른쪽 방향에서 보이는 빌딩 개수 구하기 

import sys

input = sys.stdin.readline

# 왼쪽 방향 빌딩 개수 탐색
def left_buildings(B1, B_list):
    B_list = B_list[::-1]
    max_slope = float("-inf")
    cnt = 0
    for idx in range(len(B_list)):
        B2 = B_list[idx]
        slope =  (B2 - B1) / (idx+1)
        if slope > max_slope:
            max_slope = slope
            cnt += 1
    return cnt

# 오른쪽 방향 빌딩 개수 탐색
def right_buildings(B1, B_list):
    max_slope = float("-inf")
    cnt = 0
    for idx in range(len(B_list)):
        B2 = B_list[idx]
        slope =  (B2 - B1) / (idx+1)
        if slope > max_slope:
            max_slope = slope
            cnt += 1
    return cnt

N = int(input())

B_list = list(map(int, input().split()))

max_cnt = 0

for i in range(N):
    left_cnt = left_buildings(B_list[i], B_list[:i])
    right_cnt = right_buildings(B_list[i], B_list[i+1:])
    max_cnt = max(left_cnt+right_cnt, max_cnt)

print(max_cnt)



