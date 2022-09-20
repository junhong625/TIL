T = int(input())

delta = [[-1,-1],[-1,1],[1,1],[1,-1]]   # 대각 방향의 4방위 delta 생성

## dfs와 delta 탐색을 이용해 가장 많이 먹을 때의 디저트 수 탐색
def dfs(x, y, visited, move=0):         # x좌표, y좌표, 방문기록, 이동 방향
    for dx, dy in delta[move:]:         # delta순회(과거에 갔던 방향으로는 이동 불가)
        global result                   # result 호출
        if [dx+x, dy+y] == start:       # 이동 지점이 시작점과 같을 경우
            result = max(result, len(visited))  # 디저트 수 비교
        if 0 <= dx+x < N and 0 <= dy+y < N and cafes[dx+x][dy+y] not in visited:    # 디저트 거리 안이며 방문 한 적 없는 카페일 경우
            if [dx, dy] == delta[0]:                                                # 디저트를 먹고 이동 방향에 맞춰 다음 dfs실시 
                dfs(dx+x, dy+y, visited+[cafes[dx+x][dy+y]], 0)
            elif [dx, dy] == delta[1]:
                dfs(dx+x, dy+y, visited+[cafes[dx+x][dy+y]], 1)
            elif [dx, dy] == delta[2]:
                dfs(dx+x, dy+y, visited+[cafes[dx+x][dy+y]], 2)
            else:
                dfs(dx+x, dy+y, visited+[cafes[dx+x][dy+y]], 3)

for t in range(1,T+1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            start = [i,j]
            if start not in [[0,0],[0,N-1],[N-1,N-1],[N-1,0]]:  # 끝 모서리들은 사각형을 만들 수 없기에 제외
                dfs(i, j, [cafes[i][j]])
    print(f'#{t} {result if result > 3 else -1}')               # 사각형을 그려야 하기에 4곳 이상 먹은 것만 결과 값에 해당