def check_sdoku(sdoku): # 정상적으로 숫자가 입력되어 있는지 체크하는 함수
    sdoku_std_col = [[sdoku [j][i] for j in range(9)] for i in range(9)]    # 세로와 가로를 바꾼 sdoku
    delta = [[i, j] for i in range(3) for j in range(3)]                    # 3X3 delta 생성
    
    for i in range(9):                                                      # 세로와 가로에 입력되지 않은 숫자가 있는지 체크
        for j in range(1,10):
            if j not in sdoku[i] or j not in sdoku_std_col[i]:
                return 0

    for i in range(0, 9, 3):                                                # 3X3의 모든 숫자의 합이 45 미만일 경우 오답 처리
        for j in range(0, 9, 3):
            total = 0
            for x, y in delta:
                total += sdoku[i+x][j+y]
            if total != 45:
                return 0
    return 1
    

T = int(input())

for t in range(1, T+1):
    sdoku = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{t} {check_sdoku(sdoku)}')