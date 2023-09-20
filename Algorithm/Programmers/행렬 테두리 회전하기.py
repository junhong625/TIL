# 문제: 회전한 행렬 중 최소값들 구하기

# 조건: 1) 2 <= rows, columns <= 100
#      2) 가로 방향으로 숫자가 1씩 증가
#      3) 1 <= queries <= 10000
#      4) 1 <= x1 < x2 <= rows
#      5) 1 <= y1 < y2 <= columns

# 방법: 1) x1, y1부터 시작해서 우, 하, 좌, 상 각 방향마다 이동 조건 설정

def solution(rows, columns, queries):
    grid = [[i*columns+j+1 for j in range(columns)] for i in range(rows)]
    answer = []
    
    for x1, y1, x2, y2 in queries: # 방법 1
        direction = 1
        x, y = x1-1, y1-1
        temp = grid[x][y]
        minV = float('inf')
        while direction != 5:
            minV = min(minV, grid[x][y])
            if direction == 1:
                if y == y2-1:
                    direction += 1
                    continue
                y += 1
                temp2 = grid[x][y]
                grid[x][y] = temp
                temp = temp2
                
            elif direction == 2:
                if x == x2 - 1:
                    direction += 1
                    continue
                x += 1
                temp2 = grid[x][y]
                grid[x][y] = temp
                temp = temp2
                
            elif direction == 3:
                if y == y1 - 1:
                    direction += 1
                    continue
                y -= 1
                temp2 = grid[x][y]
                grid[x][y] = temp
                temp = temp2
                
            else:
                if x == x1 - 1:
                    direction += 1
                    continue
                x -= 1
                temp2 = grid[x][y]
                grid[x][y] = temp
                temp = temp2
        
        answer.append(minV)
        
    return answer