T = int(input())

for t in range(1, T+1):
    N = int(input()) # 원소 개수
    arr = list(map(int, input().split())) # 배열
    
    for i in range(10): # 10번만 정렬
        target = i # 다음 for문에서 범위의 시작점, 짝수일 때 최대값의 idx, 홀수일 때 최소값idx  
        
        for j in range(target, N): # i부터 배열 끝까지
            
            if i % 2 == 0: # 짝수일 경우
                if arr[j] > arr[target]: # 최대값 비교
                    target = j
            
            else: # 홀수일 경우
                if arr[j] < arr[target]: # 최소값 비교
                    target = j
        
        arr[i], arr[target] = arr[target], arr[i] # 최대값(or 최소값)을 순서에 맞게 배열의 시작점부터 정렬
    
    print(f'#{t}', end=' ')
    print(*arr[:10]) # 정렬된 원소 10개만 출력