import collections

## 미생물 테스트
def test(time):
    total = 0
    for _ in range(time):
        duplicate = collections.defaultdict(list)                       
        for i in range(1, K+1):
            x, y, cnt, d = group[i]
            if area[x][y] == i:                                         # 현재 좌표에 새겨진 번호가 내 순번과 같은 번호일 경우에만 삭제
                area[x][y] = 0
            if cnt == 0:                                                # 군집이 없을 경우 다음 순회
                continue
            dx = x+dir[d][0]
            dy = y+dir[d][1]
            if dx in [0,N-1] or dy in [0,N-1]:                          # 약품이 칠해진 위치에 도착했을 경우
                cnt //= 2                                               # 군집 수 절반으로 감소
                d = dic[d]                                              # 방향을 반대로 설정
            duplicate[(dx,dy)].append([cnt, d])                         # 같은 위치에서 만나는 군집들의 방향을 설정해주기 위해 좌표 기준으로 cnt와 d를 추가
            if area[dx][dy] and area[dx][dy] < i:                       # 이동해야할 위치에 다른 군집이 존재하고 둘 다 이동을 마친 군집일 경우
                if group[area[dx][dy]][2] > cnt:                        # 이동할 위치에 존재한 군집의 수가 더 클 경우
                    group[area[dx][dy]][2] += cnt                       # 해당 군집 기준으로 현재 군집과 병합
                    dx, dy, cnt, d = 0, 0, 0, 0                         # 현재 군집 삭제
                else:                                                   # 현재 군집의 수가 더 큰 경우
                    cnt += group[area[dx][dy]][2]                       # 현재 군집 기준으로 이동할 위치에 존재한 군집과 병합    
                    group[area[dx][dy]] = [0,0,0,0]                     # 이동할 위치의 군집 삭제
            group[i] = [dx, dy, cnt, d]                                 # 현재 순번의 그룹에 좌표와 미생물 수, 방향 저장
            area[dx][dy] = i                                            # 이동한 위치에 내 순번 저장
        for dup in duplicate:                                           # 중복되는 좌표들 체크
            if len(duplicate[dup]) > 1 and area[dup[0]][dup[1]]:        # 해당 좌표에 해당하는 군집이 1개보다 많고 순번이 0번이 아닐 경우 
                group[area[dup[0]][dup[1]]][3] = max(duplicate[dup])[1] # 해당 좌표에 저장되어 있는 순번의 방향을 모여있는 군집 중 가장 큰 군집의 방향으로 변경
    for _,_,cnt,_ in group[1:]:                                         # 각 군집들의 미생물 수를 모두 더함
        total += cnt        
    return total

dir = [[],[-1,0],[1,0],[0,-1],[0,1]]                                    # 방향(방향이 1부터 4까지로 설정 되어 있기에 0은 패딩 처리)
dic = {1:2, 2:1, 3:4, 4:3}                                              # 방향 전환

T = int(input())

for t in range(1, T+1):
    N, M, K = map(int, input().split())
    area = [[0 for _ in range(N)] for _ in range(N)]
    group = [[] for _ in range(K+1)]
    for i in range(1, K+1):
        x, y, cnt, d = map(int, input().split())
        group[i] = [x,y,cnt,d]  # 군집의 정보 저장
        area[x][y] = i          # 좌표에 군집의 번호 저장
    print(f'#{t} {test(M)}')