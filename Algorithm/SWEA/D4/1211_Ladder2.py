delta = [[1, 0], [0, 1], [0, -1]] # 방향(아래, 오른쪽, 왼쪽)

def cnt_move(y, x): # 이동 횟수를 계산하는 함수
    idx = 0         # 방향(delta에 적용될 인덱스)
    cnt = 0         # 이동 횟수
    while y != 99:  # 바닥에 도착하면 종료
        if idx == 0:                                    # 아래로 내려가고 있을 경우
            if arr[y+delta[1][0]][x+delta[1][1]] == 1:  # 오른쪽 방향이 나타나면 오른쪽으로 이동
                y, x = y+delta[1][0], x+delta[1][1]
                idx = 1
            elif arr[y+delta[2][0]][x+delta[2][1]] == 1:# 왼쪽 방향이 나타나면 왼쪽으로 이동
                y, x = y+delta[2][0], x+delta[2][1]
                idx = 2
            else:                                       # 좌우 방향 모두 안 나온다면 아래로 이동
                y, x = y+delta[0][0], x+delta[0][1]     
        else:                                           # 오른쪽or왼쪽으로 가고 있을 경우
            if arr[y+delta[0][0]][x+delta[0][1]] == 1:  # 아래로 이동할 수 있다면 아래로 이동
                y, x = y+delta[0][0], x+delta[0][1]
                idx = 0
            else:                                       # 아래로 이동할 수 없다면 현재 방향 그대로 이동
                y, x = y+delta[idx][0], x+delta[idx][1]
        cnt += 1                                        # 이동 후 이동 횟수 + 1
    return cnt
    

for _ in range(10):
    t = int(input())
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)] # padding을 위해 리스트 양끝에 0을 추가
    minV = 1000                 # 최소 이동 횟수
    minV_idx = 0                # 최소 이동 횟수의 출발 idx
    for i in range(1, 101):     # padding을 했기에 0과 101을 제외
        if arr[0][i] == 1:      # 시작라인에서 1인 경우 
            cnt = cnt_move(0, i)# 해당 위치에서 이동 횟수를 계산하는 함수 실행
            # print(cnt)
            if minV >= cnt:     # 최소 이동 횟수인지 확인
                minV = cnt
                minV_idx = i-1  # padding을 했기에 -1을 해줘야 원래의 index
    print(f'#{t} {minV_idx}')
