def find_set(x):                        # 대표 원소 탐색
    while rep[x] != x:
        x = rep[x]
    return x

def union(x, y):                        # y의 그룹이 x의 그룹에 병합
    rep[find_set(y)] = find_set(x)

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    rep = [i for i in range(N+1)]       # 본인을 가리키는 정점
    
    for _ in range(M):
        s, e = map(int, input().split())
        union(s, e)                     # s와 e를 그룹으로 병합
    
    result = set()                      # 대표 원소의 개수 즉, 그룹의 개수를 판단하기 위한 변수
    for i in range(1, N+1):             # 중복을 제외한 대표 원소들을 result에 삽입
        result.add(find_set(rep[i]))
    print(f'#{t} {len(result)}')        # result의 개수 == 그룹의 수