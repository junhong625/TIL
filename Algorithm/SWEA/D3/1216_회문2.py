def len(arr):
    cnt = 0
    for a in arr:
        cnt += 1
    return cnt

for t in range(1, 11):
    T = int(input())
    row_arr = [input() for _ in range(100)] # 가로 기준 배열
    col_arr = [[row_arr[j][i] for j in range(100)]for i in range(100)] # 세로와 가로를 바꾼 배열
    result = 0
    for n in range(100,0,-1): # 배열 길이
        for i in range(100):
            j = 0 # 배열 시작 인덱스
            while j+n <= 100: # 배열 길이가 100이 될때까지 반복
                row = row_arr[i][j:j+n] # 행
                col = col_arr[i][j:j+n] # 열
                center = (n+1)//2 # 배열 중앙 인덱스 계산
                if n % 2 == 0: # 짝수일 때
                    if row[:center][::-1] == row[center:]:
                        result = result if result > len(row) else len(row)
                        break
                    if col[:center][::-1] == col[center:]:
                        result = result if result > len(col) else len(col)
                        break
                else: # 홀수일 때
                    if row[:center][::-1] == row[center-1:]:
                        result = result if result > len(row) else len(row)
                        break
                    if col[:center][::-1] == col[center-1:]:
                        result = result if result > len(col) else len(col)
                        break
                j += 1
            
    print(f'#{T} {result}')