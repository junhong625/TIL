import sys

input = sys.stdin.readline

# i,j 위치에서 각 조건의 최적값인지 체크
def check_condition(i, j, cnt, case):
    global max_adj
    if cnt > max_adj:
        max_adj = cnt
        case.clear()
        case.append((i,j))
    elif cnt == max_adj:
        case.append((i,j))

# 1번 조건으로 체크
def condition_1(num):
    global max_adj
    case = []
    max_adj = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                continue
            cnt = 0
            for dx, dy in delta:
                dx += i
                dy += j
                if 0 <= dx < N and 0 <= dy < N and grid[dx][dy] in favorite[num]:
                    cnt += 1
            check_condition(i,j,cnt,case)
    if len(case) > 1:
        case = condition_2(case)
    return case[0]

# 2번 조건으로 체크
def condition_2(input_case):
    global max_adj
    case = []
    max_adj = 0
    for i, j in input_case:
        cnt = 0
        for dx, dy in delta:
            dx += i
            dy += j
            if 0 <= dx < N and 0 <= dy < N and grid[dx][dy] == 0:
                cnt += 1
        check_condition(i,j,cnt,case)
    # 순회를 통해서 i,j가 가장 낮은 값부터 case에 넣기에 3번 조건 체크가 불필요
    return case

# 결과 값 구하기
def check_res():
    res = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for dx, dy in delta:
                dx += i
                dy += j
                if 0 <= dx < N and 0 <= dy < N and grid[dx][dy] in favorite[grid[i][j]]:
                    cnt += 1
            res += res_dic[cnt]
    return res

delta = [(0,1),(0,-1),(1,0),(-1,0)] # 4방위 좌표
res_dic = {0:0, 1:1, 2:10, 3:100, 4: 1000} # 결과 계산 시 만족도에 따른 점수 계산

N = int(input())

grid = [[0] * N for _ in range(N)]

favorite = {}   # 취향 기록
max_adj = 0     # 최적위치를 찾기 위한 최대 인접값

for _ in range(N**2):
    fav = list(map(int, input().split()))
    num, favorite[num] = fav[0], fav[1:]
    x, y = condition_1(num)
    grid[x][y] = num

print(check_res())

    
    