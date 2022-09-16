def dfs(idx, s):                    # dfs 재귀 함수 -> idx = 현재 인덱스, s = 합
    global result                   # result 호출 
    if s >= B:                      # 합이 B 이상일 경우
        result = min([result, s])   # result 와 작은 값을 비교하여 할당 후 종료
        return
    for i in range(idx+1, N):       # 현재 직원의 다음 직원부터 순회
        dfs(i, s+height[i])         # (다음 직원의 idx, 탑의 높이 + 다음 직원의 키)

T = int(input())

for t in range(1, T+1):                     
    N, B = map(int, input().split())            
    height = list(map(int, input().split()))
    result = sum(height)            # 탑의 최대 높이
    for n in range(N):              # N만큼 순회하면서 부분집합의 합을 계산
        dfs(n, height[n])
    print(f'#{t} {result-B}')