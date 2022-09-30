from collections import defaultdict

def dfs(board, line=0, point=[]):
    if line == N:
        case[len(point)] += 1
        return
    for i in range(N):
        if not point:
            board[line][i] = 1
            point.append([line, i])
            dfs(board, line+1, point)
            board[line][i] = 0
            point.pop()
        elif sum(board[line]) == 0:
            if [line,i] not in [[j, y]for x, y in point for j in range(N)]:
                if [line, i] not in [[x+j, y+j]for x, y in point for j in range(-x, N-x)]:
                    if [line, i] not in [[x+j, y-j]for x, y in point for j in range(-x, N-x)]:
                        board[line][i] = 1
                        point.append([line, i])
                        dfs(board, line+1, point)
                        board[line][i] = 0
                        point.pop()

T = int(input())

for t in range(1, T+1):
    N = int(input())
    chessboard = [[0 for _ in range(N)] for _ in range(N)]
    case = defaultdict(int)
    dfs(chessboard)
    print(f'#{t} {case[max(case)] if case else 0}')