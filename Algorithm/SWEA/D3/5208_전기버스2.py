def dfs(cur):
    global cnt
    while cur + charge_spot[cur] < N-1:                         # 현재 위치와 현재 위치에서 최대 이동 가능한 위치가 도착 지점이 아닐 경우에 반복
        max_dis, max_idx = 0, 0                                 # max_dis 최대 이동 가능 거리, max_idx : 최대 이동 가능한 위치
        for i in range(charge_spot[cur],0,-1):                  # 현재 위치에서 가장 멀리 갈 수 있는 곳부터 역순으로 탐색
            if max_dis < i + charge_spot[cur+i]:                # 최대 이동 가능한 거리보다 더 멀리 갈 수 있는 위치일 경우
                max_dis, max_idx = i + charge_spot[cur+i], i    # 최대 이동 가능 거리와 최대 이동 가능한 위치 변경
        cnt += 1                                                # 충전 횟수 + 1
        cur += max_idx                                          # 현재 위치에서 최대 이동 가능한 위치로 이동
    return cnt

T = int(input())

for t in range(1, T+1):
    arr = list(map(int, input().split()))
    N, charge_spot = arr[0], arr[1:]
    stack = [0]
    cnt = 0
    print(f'#{t} {dfs(0)}')
