import collections

## bfs를 통해 탈주범이 이동 가능한 파이프 파악
def bfs(x, y):                                              # x: 세로 좌표, y: 가로 좌표
    q = collections.deque([[x, y, 1]])                                  # q에 [좌표값, 해당 파이프까지 이동하는데 걸리는 시간] 추가 q: 이동 가능한 파이프
    total = 1                                               # 이동 가능한 파이프 개수
    visited = [[False for _ in range(M)] for _ in range(N)] # 방문 기록
    visited[x][y] = True                                    # 현재 파이프를 이동 가능한 파이프 개수에 포함한 것으로 변경
    while q:                                                # q가 존재한다면 계속 반복
        x, y, time = q.pop(0)                               # q에서 가장 앞에 있는 값을 꺼내 x, y, time에 할당
        if time == L:                                       # 해당 파이프까지 이동하는 시간이 L과 같다면 종료
            break
        for dx, dy in tunnel[arr[x][y]]:                    # 현재 터널에서 이동가능한 터널 탐색
            if 0 <=x+dx< N and 0 <=y+dy< M and not visited[x+dx][y+dy] and [-dx,-dy] in tunnel[arr[x+dx][y+dy]]: # 범위 안에 있으며 방문한 적이 없고 파이프가 서로 연결되어 있다면
                total += 1                                  # 이동 가능한 파이프 개수를 하나 더해주고
                visited[x+dx][y+dy] = True                  # 해당 파이프를 이동 가능한 파이프 개수에 포함한 것으로 변경
                q.append([x+dx, y+dy, time+1])              # 다음 탐색을 위해 q에 [해당 파이프 좌표 x,y 와 시간+1]추가
    return total                                            # bfs가 끝나고 나면 이동가능한 파이프 개수 반환

T = int(input())

# 각 터널 번호에 맞춰 delta 값 설정
tunnel = {0:[], 1:[[-1,0],[1,0],[0,-1],[0,1]], 2:[[-1,0],[1,0]], 3:[[0,-1],[0,1]],4:[[-1,0],[0,1]], 5:[[1,0],[0,1]], 6:[[1,0],[0,-1]], 7:[[-1,0],[0,-1]]}

for t in range(1,T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t} {bfs(R,C)}')   # 주어진 좌표 R,C부터 bfs를 하여 반환되는 이동 가능한 파이프 개수 출력