import sys
from collections import deque

sys.stdin = open('TIL\Algorithm\Baekjoon\Gold\input.txt', 'r')

input = sys.stdin.readline

delta = [(0,1),(1,0),(0,-1),(-1,0)]         # 4방위

## 불이 몇 초에 해당 좌표로 옮겨지는지 체크
def fire_way():             
    fire = deque()                      # 불의 좌표 리스트
    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':   # 불의 좌표 리스트에 추가
                fire.append((i,j))      
            elif building[i][j] == '@': # 상근이의 위치
                global user_x, user_y
                user_x, user_y = i, j
    cnt = 0
    while fire:                         # 퍼질 불이 존재할 경우
        cnt += 1
        for _ in range(len(fire)):      # 현재 퍼질 수 있는 불씨의 개수만큼 반복
            x, y = fire.popleft()       # x, y 불의 좌표
            for dx, dy in delta:        # 4방위에 불이 퍼질 수 있는지 체크하여 불 리스트에 추가
                dx += x
                dy += y
                if 0 <= dx < h and 0 <= dy < w and not fire_map[dx][dy] and building[dx][dy] != '#' and building[dx][dy] != '*':
                    fire_map[dx][dy] = cnt
                    fire.append((dx,dy))

## 탈출 루트 | x, y = 상근이 좌표 
def escape(x, y):
    q = deque([(x,y)])
    visited = [[0]*w for _ in range(h)] # 상근이의 탈출 루트
    visited[x][y] = 1
    cnt = 1
    while q:                            # 상근이가 이동 현재 초에 이동가능한 좌표 
        for _ in range(len(q)):
            x, y = q.popleft()
            if x == 0 or x == h-1 or y == 0 or y == w-1:    # 상근이가 빌딩 바깥으로 나갈 수 있을 경우
                return cnt
            for dx, dy in delta:        # 상근이가 이동 가능한 방향 체크
                dx += x
                dy += y
                # 1.빌딩 안 2.방문 X 3.벽 X 4.불 시작점 X 5.불길보다 빨리 지나갈 수 있거나 불길이 지나가지 않는 자리
                # 총 5가지 경우에 모두 해당할 경우
                # 상근이가 이동 
                if 0 <= dx < h and 0 <= dy < w and not visited[dx][dy] and building[dx][dy] != '#' and building[dx][dy] != '*' and (fire_map[dx][dy] > cnt or not fire_map[dx][dy]):
                    visited[dx][dy] = 1
                    q.append((dx,dy))
        cnt += 1
    return 'IMPOSSIBLE' # 탈출이 불가능한 경우

for _ in range(int(input())):
    w, h = map(int, input().split())
    building = [list(input()) for _ in range(h)]
    fire_map = [[0]*w for _ in range(h)]
    user_x, user_y = 0, 0
    fire_way()
    print(fire_map)
    print(escape(user_x, user_y))



