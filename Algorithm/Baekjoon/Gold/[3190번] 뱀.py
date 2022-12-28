import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

grid = [[0] * N for _ in range(N)]
snake = [(0, 0)]

for _ in range(K):
    x, y = map(int, input().split())
    grid[x-1][y-1] = 1

L = int(input())
rotate = []

for _ in range(L):
    rotate.append(list(map(str, input().split())))

second = 0 # 시간
rot = 0 # 0:행, 1:열
s, r = rotate.pop(0)
direction = 1 # -1:좌 1:우

while True:
    second += 1
    x, y = snake[-1] # 현재 좌표
    
    if rot == 1: # rot에 따라 x, y에 값이 더해질지 결정
        x += direction
    else:
        y += direction
    if second == int(s): # 방향을 바꿔야할 시간일 경우
        if rot == 0 and r == 'L': # 행으로 이동 시 'L'일 경우에만 좌우 전환
            direction = -direction
        elif rot == 1 and r == 'D': # 열로 이동 시 'D'일 경우에만 좌우 전환
            direction = -direction
        rot = (rot + 1) % 2 # 방향 전환
        if rotate:
            s, r = rotate.pop(0)
            print(rot, s, r)

    print(second, x, y)

    if x < 0 or x >= N or y < 0 or y >= N or (x,y) in snake: # 이동할 좌표가 범위 밖이거나 뱀의 신체부위라면 종료
        break

    snake.append((x,y)) # 뱀의 머리 이동

    if grid[x][y] == 1: # 사과가 존재할 경우
        grid[x][y] = 0 # 사과만 제거
    else: # 사과가 존재하지 않을 경우
        snake.pop(0) # 뱀의 꼬리 줄이기
    
print(second)
    