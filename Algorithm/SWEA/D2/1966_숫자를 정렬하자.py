T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(N-1): # 선택 정렬) 범위에서 가장 작은 값을 제일 좌측에 정렬
        std = i
        for j in range(i, N):
            if arr[j] < arr[i]:
                std = j 
                arr[i], arr[std] = arr[std], arr[i]
    print(f'#{t}', end=' ')
    print(*arr)