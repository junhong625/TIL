def check_word_len(arr, n, k): # 배열을 돌며 단어의 길이를 체크하는 함수
    cnt = 0
    for i in range(n):
        word_len = 0
        for check in arr[i]:
            if check == 1 :
                word_len += 1
            else:
                if word_len == k:
                    cnt += 1
                word_len = 0
        if word_len == k:
            cnt += 1
    return cnt 

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    arr_row = [list(map(int, input().split())) for _ in range(N)]   # 기본 배열 
    arr_col = [[arr_row[i][j] for i in range(N)] for j in range(N)] # 세로와 가로를 바꾼 배열
    print(f'#{t} {check_word_len(arr_row, N, K) + check_word_len(arr_col, N, K)}')