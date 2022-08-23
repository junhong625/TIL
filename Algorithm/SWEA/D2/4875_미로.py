T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    stack = []
    start, end, result = 0, 0, 1                # 시작 좌표, 도착 좌표, 결과
    for i in range(N):                          # 시작 좌표와 도착 좌표 탐색
        for j in range(N):
            if arr[i][j] == 3:
                end = [i, j]
            elif arr[i][j] == 2:
                start = [i, j]
                stack.append(start)             # 시작 좌표 스택에 추가
    
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 우,하,좌,상
    while end != start:                         # 시작 좌표와 도착 좌표가 같아지면 종료
        arr[start[0]][start[1]] = 1             # 이동한 위치 벽으로 변경
        for x, y in delta:                      # delta로 4방향 확인
            if 0 <= start[0] + x < N and 0 <= start[1] + y < N and arr[start[0]+x][start[1]+y] != 1: # 좌표가 배열 범위를 벗어나지 않고 좌표의 값이 1이 아닐 경우
                stack.append(start)                                                                  # 현재 좌표를 스택에 추가하고
                start = [start[0]+x, start[1]+y]                                                     # 이동 가능한 위치로 이동 후 탈출
                break
        else:                                   # 해당 좌표에서 더 이상 갈 곳이 없다면
            if stack:                           # 스택에 원소가 존재하면
                back = stack.pop()              # 뒤로 이동
                start = [back[0], back[1]]
            else:                               # 스택에 원소가 없다면
                result = 0                      # 더 이상 이동할 곳이 없다는 의미
                break
    print(f'#{t} {result}')