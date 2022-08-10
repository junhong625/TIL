def max(*args): # 최대값을 골라주는 함수
    result = 0
    for num in args:
        result = result if result > num else num
    return result

for _ in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_sum, sum1, sum2 = 0, 0, 0
    
    for i in range(100): # 대각 합
        sum1 += arr[i][i]
        sum2 += arr[i][99-i]

        tot1, tot2 = 0, 0
        for j in range(100): # 행, 열 합
            tot1 += arr[i][j]
            tot2 += arr[j][i]
        max_sum = max(max_sum, sum1, sum2, tot1, tot2) # 최대값 비교
    
    print(f'#{t} {max_sum}')