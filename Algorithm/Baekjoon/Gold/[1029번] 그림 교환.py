# 문제: 그림을 소유했던 사람의 수의 최댓값 계산
# 시간 제한 2초 / 메모리 제한 128MB

# 조건: 1) 그림을 팔 때, 그림을 산 가격보다 크거나 같은 가격으로 판매
#      2) 같은 그림을 두 번 이상 사는 것은 불가능
#      3) 2 <= N <= 15
#      4) 0 <= 가격 <= 9

# 방법: 1) DFS와 비트마스킹, DP를 통해서 각 좌표의 최대 인원(이동 거리) 계산
#      2) 계산 본인 포함 최대 인원이니까 + 1
#      + DP를 (현재 좌표, 방문기록)으로 저장하면 이전과 DP에 존재하는 접근 방식과 다른 방식으로 접근했을 때의 루트가 차단되어버림
#      -> 따라서 pre_price까지 더해 (현재 좌표, 방문 기록, pre_price)와 같은 방식으로 저장해야 더 나은 접근 방식을 차단하지 않을 수 있음
#      ex)  
#      5
#      01199
#      00530
#      02060
#      00004
#      00000
#      정답 : 5
#      3차원으로 계산하지 않을 경우 4가 출력됨

import sys

input = sys.stdin.readline

N = int(input())

adjList = [input().rstrip() for _ in range(N)]
dp = {}

def dfs(pre_price, idx, visited): # 방법 1
    if visited == (1 << N) - 1: # 모든 곳을 방문했다면 종료
        return dp[(idx, visited, pre_price)]

    if (idx, visited, pre_price) in dp: # 이 작업을 했었다면
        return dp[(idx, visited, pre_price)]

    max_cnt = 0
    for i in range(1, N):
        if idx == i or visited & (1 << i) or int(adjList[idx][i]) < pre_price:
            continue
        cnt = dfs(int(adjList[idx][i]), i, visited | (1 << idx)) + 1
        max_cnt = max(max_cnt, cnt)
    dp[(idx, visited, pre_price)] = max_cnt
    return max_cnt

print(dfs(0, 0, 1) + 1) # 방법 2