# 조건: x에서 y까지 이동하는데 걸리는 최단 작동 횟수
# 고려사항: 1) x에서 y지점에 도착할때 1광년만 이동해서 도착해야함
#         2) 0이하로 이동하는건 의미 없음
# 방법: 1) bfs로 풀이하되 q에 탐색 케이스를 추가하는 시점에 고려사항을 조건으로 추가(입력값의 최대 크기가 2의 31승이라 메모리 초과로 실패)
#      2) 이동 거리의 증가에 따른 횟수 증가 규칙이 존재 -> 이동 횟수가 홀수가 될 때마다 횟수의 반복이 +1 됨(1, 2, 33, 44, 555, 666, 7777, 8888)
#       ex) 이동 거리 |  횟수  | x -> y
#               1   |   1   |   1
#               2   |   2   |   11
#               3   |   3   |   111
#               4   |   3   |   121
#               5   |   4   |   1211
#               6   |   4   |   1221
#               7   |   5   |   12211
#               8   |   5   |   12221
#               9   |   5   |   12321
#               10  |   6   |   123211
#               11  |   6   |   123221
#               12  |   6   |   123321
#               13  |   7   |   1233211
#               14  |   7   |   1233221
#               15  |   7   |   1233321
#               16  |   7   |   1234321

import sys

input = sys.stdin.readline

def pattern(n):
    moving_count = 0 # 이동 횟수
    repeat_count = 0 # 반복 횟수
    num = 0
    
    while num < n:
        moving_count += 1
        if moving_count % 2 == 1:
            repeat_count += 1
        num += repeat_count
    return moving_count

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())

    print(pattern(y-x))