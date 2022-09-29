## 최소 비용을 구하는 함수
def dijkstra():
    q = [0 for i in range(N*N**2)]                                                          # q 생성
    front, rear = -1, -1                                                                    # 포인터 설정
    rear += 1                                                                               # enque
    q[rear] = [0,0]                                     
    minDIS[0][0] = 0                                                                        # 현재 위치에 대한 최소 비용은 0
    
    while front != rear:                                                                    # q가 없어질 때 까지
        front += 1                                                                          # deque
        x, y = q[front]
        # delta = []                                                                        # 높이에 따라서 좌표가 나오는 순서 정렬
        # for dx, dy in [[0,1], [1,0], [0,-1], [-1,0]]:
        #     dx += x                                    
        #     dy += y
        #     if 0 <= dx < N and 0 <= dy < N:
        #         delta.append([Map[dx][dy], dx, dy])
        # delta.sort()

        # for v, dx, dy in delta:
        for dx, dy in [[0,1], [1,0], [0,-1], [-1,0]]:                                       # delta 순회 
            dx += x
            dy += y
            if 0 <= dx < N and 0 <= dy < N:                                                 # 범위 안일 경우
                h = Map[dx][dy]                                                             # 이동할 위치의 높이
                if Map[x][y] >= h and minDIS[dx][dy] > minDIS[x][y] + 1:                    # 이동할 위치의 높이가 현재 위치 보다 높고 이동할 위치의 최소 비용이 현재 위치에서도 이동 비용의 합 보다 높을 경우
                    minDIS[dx][dy] = minDIS[x][y] + 1                                       # 이동할 위치의 최소 비용 변경
                    rear += 1                                                               # enque
                    q[rear] = [dx,dy]
                elif Map[x][y] < h and minDIS[dx][dy] > minDIS[x][y] + (h - Map[x][y]) + 1: # 이동할 위치의 높이가 현재 위치 보다 높지 않고 이동할 위치의 최소 비용이 현재 위치에서도 이동 비용의 합 보다 높을 경우
                    minDIS[dx][dy] = minDIS[x][y] + (h - Map[x][y]) + 1                     # 이동할 위치의 최소 비용 변경
                    rear += 1                                                               # enque
                    q[rear] = [dx,dy]
    return minDIS[N-1][N-1]                                                                 # 반복문이 끝난 후 도착지점의 좌표 값 출력

T = int(input())

for t in range(1, T+1):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]
    minDIS = [[float('inf') for _ in range(N)] for _ in range(N)]
    print(f'#{t} {dijkstra()}')