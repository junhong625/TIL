def dfs(p, cnt=1):
    global max_p
    if p <= max_p:                                                  # 현재 확률이 최대 확률 이하일 경우 종료(가지치기)
        return                                                  

    if cnt == N and max_p < p:                                      # 모든 인원이 일을 했고 현재 확률이 최대 확률보다 클 경우
        max_p = p                                                   # 최대 확률을 현재 확률로 변경
        return

    for idx, value in enumerate(percent[cnt]):                      # 현재 순서에 일할 경우 각 인원들의 성공 확률을 순회
        if not visited[idx]:                                        # 일하지 않은 인원일 경우
            visited[idx] = True                                     # 일한 것으로 변경
            dfs(p * (value * 0.01), cnt+1)                          # 현재 확률에 해당 인원의 성공 확률을 곱한 값과 횟수 + 1 한 후 다음 순번에 남은 인원들 확률 탐색
            visited[idx] = False                                    # 다음 탐색을 위해 초기화
        
T = int(input())

for t in range(1,T+1):
    N = int(input())
    percent = [list(map(int, input().split())) for _ in range(N)]
    if N > 1:
        visited = [False for _ in range(N)]
        max_p = 0
        for i in range(N):
            visited[i] = True
            dfs(percent[0][i])
            visited[i] = False
        print(f'#{t} {max_p:.6f}')
    else:
        print(f'#{t} {percent[0][0]:.6f}')

## visited를 사용하지 않고 풀어보려한 코드
## 정답은 나오지만 시간이 굉장히 오래 걸림        
# from collections import deque

# def dfs(group, p, cnt=1):
#     global max_p
#     if p <= max_p:
#         return
        
#     if cnt == N-1:
#         p *= percent[cnt][list(group.keys())[0]]/100
#         if max_p < p:
#             max_p = p
#         return 
#     for idx in sorted(percent[cnt], key=lambda x:percent[cnt][x], reverse=True):
#         value = percent[cnt][idx]
#         nums = deque()
#         for i in range(cnt, N):
#             nums.append(percent[i][idx])
#             del percent[i][idx]
#         dfs(percent[cnt+1], p * value / 100, cnt + 1)
#         for i in range(cnt, N):
#             percent[i][idx] = nums.popleft()

# T = int(input())

# for t in range(1, T+1):
#     N = int(input())
#     percent = [list(map(int, input().split())) for _ in range(N)]
#     if N > 1:
#         worker = deque([i for i in range(N)])
#         for i in range(len(percent)):
#             percent[i] = {idx:v for idx, v in enumerate(percent[i])}
            
#         max_p = 0
#         for idx in sorted(percent[0], key=lambda x:percent[0][x], reverse=True):
#             value = percent[0][idx]
#             nums = deque()
#             for i in range(1, N):
#                 nums.append(percent[i][idx])
#                 del percent[i][idx]
#             dfs(percent[1], value)
#             for i in range(1, N):
#                 percent[i][idx] = nums.popleft()
#         print(f'#{t} {max_p:.6f}')
#     else:
#         print(f'#{t} {percent[0][0]:.6f}')