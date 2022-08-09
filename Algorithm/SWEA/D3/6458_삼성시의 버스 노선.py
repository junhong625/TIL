T = int(input())

for t in range(1, T+1): # 테스트 케이스만큼 반복
    N = int(input()) # 노선 수
    bus_map_list = [] # 노선들이 담길 리스트

    for n in range(N): # 노선 수만큼 반복
        A, B = map(int,input().split()) # 노선 시작과 끝
        bus_map_list.append([A, B]) # 노선을 노선 리스트에 추가
    P = int(input()) # C정류장 개수
    print(f'#{t}', end=' ')

    for j in range(P): # 정류장 개수만큼 반복
        C = int(input()) # C번 정류장
        cnt = 0 # C번 정류장에 오는 버스 수
        for a, b in bus_map_list: # bus_map_list에서 노선을 하나씩 꺼내 
            if a <= C and b >= C: # C번 정류장을 지나가는지 확인
                cnt += 1 # 지나갈 경우 + 1
        print(cnt, end=' ')
    print()

