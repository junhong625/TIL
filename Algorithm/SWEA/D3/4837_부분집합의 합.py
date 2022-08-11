def sum(arr): # 내장함수 sum의 역할
    tot = 0
    for a in arr:
        tot += a
    return tot

def len(arr): # 내장함수 len의 역할
    tot = 0
    for a in arr:
        tot += 1
    return tot

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [i for i in range(1, 13)]
    cnt = 0 
    for i in range(1, 1 << 12): # 부분집합이 생길 수 있는 경우의 수만큼
        subset_sum = [] # 부분집합
        for j in range(12):
            if i & (1<<j) : # 부분집합 생성
                subset_sum.append(arr[j]) 
        if len(subset_sum) == N and sum(subset_sum) == K: # 생성된 부분집합의 길이가 N과 같고 합이 K와 같을 경우
            cnt += 1
    print(f'#{t} {cnt}')
