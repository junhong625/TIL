## dfs탐색을 통해 조합으로 나올 수 있는 식재료 모음 중 딱 절반만큼 구하는 함수
def dfs(cur=0, s=[0]):                              # cur : 현재 음식, s : 식재료 모음
    if len(s) == N//2:                              # 식재료 절반이 s에 찼을 경우 foods에 추가하고 반환
        foods.append(s)
    for i in range(cur+1, N):                       # 조합을 구하는 반복문
        if i not in s:
            dfs(i, s+[i])

# 식재료 모음에서 재료를 2가지 씩 조합해 나오는 시너지들을 total에 모두 더해 반환하는 함수
def synergy_sum(foods):                             # foods : 식재료 모음
    total = 0                                       # 시너지의 합
    for i in range(len(foods)):
        for j in range(i+1, len(foods)):
            total += (S[foods[i]][foods[j]] + S[foods[j]][foods[i]])
    return total
    
T = int(input())

for t in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    foods = []                                                                  # 식재료 모음들이 들어갈 리스트
    result = 20000                                                              # 최대 시너지 설정
    dfs()                                                                       # dfs 탐색을 통해 가능한 식재료 모음 모두 foods에 추가
    for A in foods:                                                             # foods에서 음식 A를 하나씩 꺼내서 순회
        B = [i for i in range(N) if i not in A]                                 # 음식 A의 반대되는 음식 B(즉, 음식 A 안에 들어있지 않은 음식들을 모아둔 리스트)
        result = min(result, abs(synergy_sum(A)- synergy_sum(B)))               # result와 A의 시너지 합에서 B의 시너지 합을 뺀 절댓값 중 더 작은 값을 result에 할당
    print(f'#{t} {result}')
        
