T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    result = ''
    for i in range(N):
        row = ''
        for j in range(N-M+1): # 가로 palindrome 확인
            row = arr[i][j:j+M]
            if row == row[::-1]:
                result = row
            column = '' 
            for k in range(j, j+M): # 세로 palindrome 확인
                column += arr[k][i]
            if column == column[::-1]:
                result = column
    print(f'#{t} {result}')