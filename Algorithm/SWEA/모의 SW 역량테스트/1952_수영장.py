def dfs(m=0, pay=0):                            # dfs 탐색을 통해 가능한 모든 금액 추가
    if m >= 12:                                 # 12월을 지나칠 시 금액을 result에 추가하고 종료
        result.append(pay)
        return
    dfs(m+1, pay + month[m] * payment[0])       # 일 계산 요금
    if month[m]:                                # 월 계산 요금
        dfs(m+1, pay + payment[1]) 
    if month[m] and month[m+1] and month[m+2]:  # 3개월 계산 요금
        dfs(m+3, pay + payment[2])     
    
T = int(input())

for t in range(1, T+1):
    payment = list(map(int, input().split()))
    month = list(map(int, input().split())) + [1,1] # 11월과 12월에 3개월치 요금 계산이 가능하도록 하기 위해
    result = []
    dfs() # dfs 탐색 시작

    # 일년치 요금과 가능한 모든 요금들 중 가장 작은 요금과 비교하여 더 작은 요금 출력
    print(f'#{t} {payment[3] if payment[3] < min(result) else min(result)}') 