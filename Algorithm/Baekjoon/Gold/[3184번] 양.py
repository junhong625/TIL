import sys

input = sys.stdin.readline

R, C = map(int, input().split())

backyard = [list(str(input())) for _ in range(R)]   # 뒷마당
visited = [[0]*C for _ in range(R)]                 # 방문 확인
delta = [(0,1),(0,-1),(1,0),(-1,0)]                 # 4방위
answer = [0,0]                                      # 양, 늑대 수

def bfs(x, y):                                      # 넓이 탐색
    sheep = 0
    wolf = 0
    q = [(x, y)]                                    # 시작 지점
    visited[x][y] = 1                               # 방문 기록

    while q:                                        # 영역 탐색
        x, y = q.pop(0)                             # 탐색 시작 위치
        if backyard[x][y] == 'o':                   # 현재 위치에 양이 존재할 경우
            sheep += 1
        elif backyard[x][y] == 'v':                 # 현재 위치에 늑대가 존재할 경우
            wolf += 1
        for dx, dy in delta:                        # 4방위 순회
            dx += x
            dy += y
            # 범위 안, 방문 X, 울타리 X 일 경우 
            if 0 <= dx < R and 0 <= dy < C and not visited[dx][dy] and backyard[dx][dy] != '#':
                visited[dx][dy] = 1                 # 방문 처리
                q.append((dx, dy))                  # 탐색 위치 리스트에 추가
    if sheep > wolf:                                # 영역 내에 양이 늑대보다 많을 경우
        return [sheep, 0]
    else:                                           # 영역 내에 늑대가 양보다 많거나 같을 경우
        return [0, wolf]

for i in range(R):
    for j in range(C):
        # 방문한 적이 없고 울타리가 아닐 경우 넓이 탐색
        if not visited[i][j] and backyard[i][j] != '#':
            result = bfs(i, j)                      # 양, 늑대 수 변수에 저장
            answer[0] += result[0]
            answer[1] += result[1]

print(*answer)
