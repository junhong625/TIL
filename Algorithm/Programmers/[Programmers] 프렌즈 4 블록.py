def solution(m, n, board):
    answer = 0
    delta = [(1,1),(0,1),(1,0),(0,0)]       # 2*2의 리스트 좌표 역순
    new_board = [[0]*m for _ in range(n)]   # 제거된 블록을 대체하기 편하게 만들기 위해 오른쪽으로 90도 회전한 보드 생성
    pang = set()                            # 그룹이 형성되어 제거될 블록들 모음
    
    # 보드를 오른쪽으로 90도 회전
    for i in range(m):
        for j in range(n):
            new_board[j][i] = board[i][j]  
    for i in range(n):
        new_board[i] = new_board[i][::-1] 
    
    # pang(=제거할 블록)이 존재하지 않으면 정지 
    while True:
        for i in range(n-1):                # 2X2 범위를 확인해야 하기에 n,m범위에 -1한 범위까지만 확인
            for j in range(m-1):
                for dx, dy in delta:
                    dx += i
                    dy += j
                    if new_board[i][j] != new_board[dx][dy] or new_board[dx][dy] == 'X': # 보드가 서로 다르거나 제거된 블록을 표시하는 X가 존재할 경우 종료 
                        break
                else:
                    for dx, dy in delta:    # 같은 캐릭터의 4개 블록이 2X2로 붙어 있는 경우 pang에 추가
                        dx += i
                        dy += j
                        pang.add((dx,dy))
        if not pang:                        # 제거할 블록이 없을 경우 종료
            break
        pang = sorted(list(pang), key=lambda x:x[1], reverse=True)  # pang을 리스트로 변경, 리스트 뒤에서부터 제거를 위해 정렬
        answer += len(pang)                 # 제거할 블록의 개수를 answer에 더하기

        for x, y in pang:                   # 블록 제거하고 한칸 땡긴 후 'X'로 삭제된 블록 대체
            new_board[x].pop(y)
            new_board[x].append('X')
        pang = set()                        # 빈 pang 생성
    return answer