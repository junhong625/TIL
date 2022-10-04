import sys

input = sys.stdin.readline

def bfs(x, y):
    babyshark = [2, 0, 0]                                   # 현재 몸집, 먹은 물고기 수, 엄마 상어 도움 없이 돌아다닌 시간
    q = []                                                  # 이동할 수 있는 장소
    q.append((x, y, 0))                                     # 현재 위치 x, y와 cnt 0을 추가
    front = -1                                              # deque를 할 위치 포인터
    visited = [[0 for _ in range(N)] for _ in range(N)]     # 간 곳인지 판단
    visited[x][y] = 1                                       # 시작점 이동한 것으로 판단
    while front != len(q)-1:                                # deque의 포인터가 q의 길이와 같아질 경우 종료
        case = []                                           # 같은 거리에서 물고기를 먹을 수 있는 경우의 수가 담길 리스트
        for _ in range(front+1, len(q)):                    # 같은 거리를 for문을 통해 한 번에 순회
            front += 1                                      # deque
            a, b, cnt = q[front]
            for dx, dy in delta:                            # 4방위 델타 순회
                dx += a
                dy += b
                if 0 <= dx < N and 0 <= dy < N:             # 범위 안이고
                    if 0 <= sea[dx][dy] and sea[dx][dy] <= babyshark[0] and not visited[dx][dy]:    # 이동할 수 있는 위치이고
                        if 0 < sea[dx][dy] < babyshark[0]:  # 먹을 수 있는 물고기일 경우
                            case.append([dx, dy])           # 먹을 수 있는 경우의 수에 해당 좌표를 추가
                        q.append((dx, dy, cnt+1))           # q에 해당 좌표와 cnt+1한 값을 추가
                        visited[dx][dy] = 1                 # 해당 좌표 방문 처리

        if case:                                            # 먹을 수 있는 경우의 수가 있을 경우
            case.sort()                                     # x,y순으로 정렬
            dx, dy = case[0]                                # 가장 위, 가장 왼쪽에 존재한 물고기 좌표를 dx와 dy로 지정
            sea[dx][dy] = 0                                 # 해당 좌표의 물고기 냠냠
            babyshark[1] += 1                               # 먹은 물고기 수 + 1
            babyshark[2] += cnt+1                           # 엄마 상어의 도움 없이 이동한 시간 추가
            ## 기본 값 모두 초기화
            visited = [[0 for _ in range(N)] for _ in range(N)] # 방문기록 초기화
            visited[dx][dy] = 1                             # dx, dy를 시작지점으로 하여 방문처리
            front = -1                                      # deque를 위한 포인터 초기화
            q = []                                          # q 초기화
            q.append((dx, dy, 0))                           # 물고기를 먹은 좌표를 시작지점으로 추가
            if babyshark[1] == babyshark[0]:                # 만약 상어가 자기 크기만큼 물고기를 먹었을 경우 
                babyshark = [babyshark[0]+1, 0, babyshark[2]]   # 사이즈 업

    return babyshark[2]                                     # 이동한 시간 출력

N = int(input())

sea = [list(map(int, input().split())) for _ in range(N)]

delta = [(-1,0), (0,-1), (1,0), (0,1)]

for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            sea[i][j] = 0
            print(bfs(i, j))