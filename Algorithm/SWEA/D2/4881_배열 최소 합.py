def backtracking(x, s):
    global min_sum
    
    if s >= min_sum:    # 가지치기
        return
    
    if x == N-1:        # 끝에 도달 시 종료
        min_sum = min_sum if min_sum < s else s # 최소값 비교
        return
    
    for j in range(N):  # N만큼 순회
        if j not in stack:  # j가 stack에 포함되어 있지 않을 경우  
            stack.append(j) # stack에 j 추가
            backtracking(x+1, s+arr[x+1][j]) # j를 stack에 추가한 상태로 재귀 실행
            stack.pop()     # j를 stack에서 제거(다음 경우의 수를 위해 원상 복귀)

T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    min_sum = N * 10 # 배열의 자리에 들어갈 수 있는 최대값이 10이기에 시작값을 배열 길이 * 10으로 설정

    for j in range(N): # 첫 번째 행부터 백트래킹 실행
        stack.append(j)
        backtracking(0, arr[0][j])
        stack.pop()
    print(f'#{t} {min_sum}')