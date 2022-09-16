from collections import deque

T = int(input())

def bfs(x, y):                                                      # bfs 탐색
    q = deque([[x, y, 1]])                                          # q에 [현재 좌표 x, 현재 좌표 y, 이동한 방 개수] 추가 
    max_cnt = 0                                                     # 현재 시작점에서 이동 가능한 최대 이동 개수
    while q:                                                        # q가 존재할 경우 계속 반복
        x, y, cnt = q.popleft()                                     # q에서 현재 좌표 x, 현재 좌표 y 이동한 방 개수를 꺼내 각 변수에 할당
        max_cnt = max([max_cnt, cnt])                               # 현재 횟수와 최대 이동 횟수 비교
        for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:                  # delta로 4방위 탐색
            if 0 <= x+dx < N and 0 <= y+dy < N and room_arr[dx+x][dy+y] == room_arr[x][y] + 1: # 이동 가능한 방이고 해당 방이 현재 방의 번호보다 1이 크다면
                q.append([x+dx, y+dy, cnt + 1])                     # q에 [해당 방 좌표 x, 해당 방 좌표 y, 이동한 방 개수]
    return max_cnt                                                  # bfs가 끝난 후 최대 이동 횟수 반환

for t in range(1, T+1):
    N = int(input())
    room_arr = []                                                   # 방 배열
    result = [N**2, 0]                                              # 정답을 [가장 큰 방 번호, 가장 적은 이동 횟수]로 설정
    for _ in range(N):                                              # 방 배열 추가
        room_arr.append(list(map(int, input().split())))
    for i in range(N):                                              # 각 방마다 bfs탐색
        for j in range(N):
            cnt = bfs(i, j)                                         # 반환된 최대 횟수를 cnt에 저장
            if cnt > result[1] or (cnt == result[1] and room_arr[i][j] < result[0]): # cnt가 현재 정답에 담겨있는 이동 횟수보다 크거나 cnt가 이동횟수와 같고 방 번호가 더 작은 경우 result를 변경
                result = [room_arr[i][j], cnt]
    print(f'#{t} {result[0]} {result[1]}')                          # 조건에 맞게 출력
    