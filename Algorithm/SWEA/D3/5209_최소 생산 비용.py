def dfs(total, cnt=1):
    global minV
    if total >= minV:                                                   # 합이 최소값보다 작을 경우 종료
        return

    if cnt == N and minV > total:                                       # 더한 횟수가 N만큼이고 최솟값보다 합이 클 경우 
        minV = total                                                    # 합을 최소값으로 변경
        return

    for idx, value in enumerate(cost[cnt]):                             # cnt의 라인에 해당하는 비용들의 위치와 비용을 순회
        if not visited[idx]:                                            # 생산하지 않은 곳일 경우
            visited[idx] = True                                         # 생산한 곳으로 변경
            dfs(total + value, cnt+1)                                   # 합에 현재 비용을 더해주고 횟수에 + 1
            visited[idx] = False                                        # 다음 dfs를 위해 생산하지 않은 곳으로 초기화
        
T = int(input())

for t in range(1,T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    if N > 1:
        visited = [False for _ in range(N)]
        minV = 99 * N                                                   # 최대값은 공장의 최대 비용인 99를 N만큼 곱해준 값으로 설정
        for i in range(N):
            visited[i] = True
            dfs(cost[0][i])
            visited[i] = False
        print(f'#{t} {minV}')
    else:
        print(f'#{t} {cost[0][0]}')
