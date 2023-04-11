import sys

input = sys.stdin.readline

N, K= map(int, input().split())
S = list(map(int, input().split()))

end = 0 # 시작점
res = 0 # 최대 길이
tmp = 0 # 부분 수열에 포함된 짝수 개수
cnt = 0 # 부분 수열에 포함된 홀수 개수

for start in range(N):
    while cnt <= K and end < N:
        if S[end] % 2 == 0: # 짝수일 경우
            tmp += 1
        else:               # 홀수일 경우
            cnt += 1
    
        end += 1
    
        # S의 시작부터 끝까지 끊이지 않고 연결된 경우
        if start == 0 and end == N: 
            res = tmp
            break
    
    # 가장 긴 짝수 연속한 부분 수열이기에 불가능해 지는 지점인 cnt == K + 1인 시점의 tmp길이를 체크 
    if cnt == K+1:
        res = max(res, tmp)

    # 시작위치를 넘길 경우
    if S[start] % 2 == 0:   # 시작 숫자가 짝수일 경우 tmp -= 1
        tmp -= 1
    else:                   # 시작 숫자가 홀수일 경우 cnt -= 1
        cnt -= 1
print(res)    
    
