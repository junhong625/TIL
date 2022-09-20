T = int(input())

def dfs(s='', x=0, y=0):
    if len(s) == 7: # 7자리수일 경우 result에 추가하고 종료
        result.add(s)
        return

    for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]: # delta를 통해 4방위 dfs 탐색
        if 0 <= dx+x < 4 and 0 <= dy+y < 4:
            dfs(s+str(arr[dx+x][dy+y]), dx+x, dy+y)

for t in range(1, T+1):
    arr = [list(map(int, input().split())) for i in range(4)]
    result = set() # set자료형으로 중복 제거
    for i in range(4):
        for j in range(4):
            dfs(str(arr[i][j]),i, j)
    # print(sorted(list(result)))
    print(len(result))