def SequentialSearch(s, x=0, y=0):                              # 완전탐색
    if [x, y] == [N-1, N-1]:                                    # 제일 오른쪽 아래 지점에 도착했을 경우
        global minV                                             # minV 호출
        minV = min(minV, s)                                     # s와 minV중 작은 값을 minV에 저장
    for dx, dy in [[0,1], [1,0]]:                               # 오른쪽 방향과 왼쪽 방향으로만 진행
        if x + dx < N and y + dy < N:                           # 범위 안일 경우
            SequentialSearch(s+arr[x+dx][y+dy], x+dx, y+dy, )   # 완전 탐색 실행

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = N * 13
    SequentialSearch(arr[0][0])
    print(f'#{t} {minV}')