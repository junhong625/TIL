def check_WB(a, b): # 시작점이 흰색일 경우 체크
    cnt = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:    
                    if chess_board[a+i][b+j] != 'W':
                        cnt += 1
                else:
                    if chess_board[a+i][b+j] != 'B':
                        cnt += 1
            else:
                if j % 2 == 0:    
                    if chess_board[a+i][b+j] != 'B':
                        cnt += 1
                else:
                    if chess_board[a+i][b+j] != 'W':
                        cnt += 1
    return cnt

def check_BW(a, b): # 시작점이 검은색일 경우 체크
    cnt = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 1:    
                    if chess_board[a+i][b+j] != 'W':
                        cnt += 1
                else:
                    if chess_board[a+i][b+j] != 'B':
                        cnt += 1
            else:
                if j % 2 == 1:    
                    if chess_board[a+i][b+j] != 'B':
                        cnt += 1
                else:
                    if chess_board[a+i][b+j] != 'W':
                        cnt += 1
    return cnt
    
N, M = map(int, input().split())
chess_board = [input() for _ in range(N)]
min_result = []
for i in range(N-8+1):
    for j in range(M-8+1):
        min_result.append(min(check_BW(i,j), check_WB(i,j)))
print(min(min_result))