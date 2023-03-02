import sys, pprint

input = sys.stdin.readline

# field를 왼쪽 방향 90도 회전하기
def turn_left(dummy):
    field = [[0]*12 for _ in range(6)]
    for j in range(6):
        for i in range(12):
            field[j][-(i+1)] = dummy[i][j]
    return field

# bfs 탐색 후 같은 블록 4개 이상 붙어있을 경우 해당 블록들 좌표 반환
def bfs(x,y, visited):
    visited[x][y] = 1
    q = [(x,y)]
    front, real = 0, 0                      # 같은 블록 묶음들을 q를 통해 확인하기 위해서 deque가 아닌 front, rear을 이용한 방식으로 bfs 탐색
    delta = [(0,1),(0,-1),(1,0),(-1,0)]
    std = field[x][y]

    while front <= real:
        x, y = q[front]
        for dx, dy in delta:
            dx += x
            dy += y
            if 0 <= dx < 6 and 0 <= dy < 12:
                if field[dx][dy] == std and not visited[dx][dy]:
                    q.append((dx,dy))
                    real += 1
                    visited[dx][dy] = 1
        front += 1
    return sorted(q, key=lambda x:x[1]) if len(q) > 3 else []

# 연쇄 반응이 나오지 않을때까지 반복
def puyo():
    cnt = 0
    while True:
        visited = [[0] * 12 for _ in range(6)]
        boom = []
        for i in range(6):
            for j in range(12):
                if field[i][j] != '.' and not visited[i][j]:
                    boom.extend(bfs(i, j, visited))

        # bfs탐색으로 나온 블록들 한 번에 제거
        if boom:
            cnt += 1
            for x, y in boom[::-1]:
                field[x].pop(y)
                field[x].append('.')
        else:
            break
        # pprint.pprint(field)
    return cnt

dummy = [list(input().rstrip()) for _ in range(12)]
field = turn_left(dummy) 

print(puyo())