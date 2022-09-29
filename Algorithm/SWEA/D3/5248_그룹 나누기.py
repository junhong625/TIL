def find_set(x):                            # 대표 원소 탐색 함수
    while group[x] != x:                    # 자기 자신을 가리킬 때까지 반복
        x = group[x]
    return x

def union(x, y):                            # 병합 함수
    group[find_set(y)] = find_set(x)        # y의 대표 원소가 x의 대표 원소를 가리키도록 설정

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    group = [i for i in range(N+1)]         # 자기 자신을 가리키는 리스트 생성
    pair = list(map(int, input().split()))  # 짝
    for i in range(0, len(pair), 2):        # 짝지어주기
        union(pair[i], pair[i+1])

    result = set()
    for i in group[1:]:                     # result에 대표 원소들을 중복제거하고 넣기 
        result.add(find_set(i))
    print(f'#{t} {len(result)}')       