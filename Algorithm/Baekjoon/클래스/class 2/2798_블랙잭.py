import sys

def blackjack(n, t, s): # n : 카드 수, t : 목표 숫자, s : 카드 합
    if s > t:           # 현재 합이 목표 숫자를 넘을 경우 종료
        return
    if n == 3:          # 카드 수가 3장이 됐을 때 
        sit.append(s)   # 현재 합을 삽입
        return
    for i in range(N):  # 카드의 수만큼 순회
        if not visited[i]:  # 사용하지 않은 카드일 경우
            visited[i] = True # 사용한 것으로 변경
            blackjack(n+1, t, s+Nums[i]) # 현재 합에 카드 숫자를 더하고 재귀 실행   
            visited[i] = False# 다음 경우의 수를 위해 초기화

N, M = map(int, sys.stdin.readline().split())

Nums = list(map(int, sys.stdin.readline().split()))
visited = [False] * N   # 카드를 사용했는지 확인
sit = []                # 카드 합의 모든 경우의 수

blackjack(0, M, 0)
print(max(sit))         # 가능한 경우의 수 중 가장 큰 수 출력