from functools import reduce

def harvest():
    def subsets(c, g=[0]):
        if sum(g) <= C:
            nonlocal case
            case.append(g)
        if len(g) == M+1:
            return
        for i in range(M):
            if not visited[i]:
                visited[i] = 1
                subsets(c, g+[c[i]])
                visited[i] = 0
    all_case = []
    for line in range(N):
        line_case = []
        for i in range(N-M+1):
            honey = [area[line][i+j] for j in range(M)]
            maxV = 0
            if sum(honey) > C:
                case = []
                visited = [0] * M
                subsets(honey)
                for j in case:
                    if sum(j) <= C:
                        maxV = max(maxV, reduce(lambda x,y:x+y**2, j))
            else:
                for j in range(M):
                    maxV += area[line][i+j] ** 2
            line_case.append(maxV)
        all_case.append(line_case)
    return all_case
    
def check_maxV(v, x, y):
    for i in range(len(case)):
        for j in range(len(case[0])):
            if [i,j] not in [[x, y+i] for i in range(-(M-1), M)]:
                global maxV
                maxV = max(maxV, v+case[i][j])

T = int(input())

for t in range(1, T+1):
    N, M, C = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]
    case = harvest()
    maxV = 0
    print(case)
    for i in range(len(case)):
        for j in range(len(case[0])):
            check_maxV(case[i][j], i, j)
    print(f'#{t} {maxV}')
    
