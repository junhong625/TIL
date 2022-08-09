T = int(input())

for t in range(1, T+1):
    K, N, M = map(int, input().split())
    bus_map = list(map(int, input().split()))
    position, cnt = 0, 0 # 버스의 위치와 충전 횟수
    while position + K < N: # 버스 위치에서 최대 이동거리만큼 이동해도 종점에 도달하지 못할 경우 반복
        for i in range(position + K, position, -1): # 버스 현재 위치와 최대 이동거리를 더한 값부터해서 버스 위치 + 1까지 역순으로 반복
            if i in bus_map: # 충전기가 설치 되어 있을 경우
                position = i # 버스를 해당 충전기 위치로 이동
                cnt += 1 # 충전 횟수 + 1
                break # 충전했으니 다시 이동
        else: # 위 반복문에서 break를 통해 탈출을 하지 못 했다는 건 현재 위치에서 최대 이동 거리 내에 충전기가 없다는 뜻 즉, 종점에 도착 불가
            position = N # while문에서 탈출하기 위해 position을 종점 값으로 할당
            cnt = 0 # 0을 출력하기 위해 0으로 할당 
    print(f'#{t} {cnt}')
