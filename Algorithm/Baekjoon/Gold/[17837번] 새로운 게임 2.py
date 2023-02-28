import sys

input = sys.stdin.readline

N, K = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
chess_pieces = {}                               # {좌표: [체스말]} 형태의 dict
pieces_position = []                            # 각 체스말들의 위치
direction = [(), (0,1), (0,-1), (-1,0), (1,0)]  # 번호(idx)에 따른 방향
d_change = {1:2, 2:1, 3:4, 4:3}                 # 방향 전환 dict

## 말들의 좌표가 겹칠 경우 리스트 형식으로 체스 말들을 삽입 
# i: 순서, d: 방향, key: 좌표 (ex: (x,y))
for i in range(K):
    x, y, d= map(int, input().split())
    key = x-1, y-1
    pieces_position.append((key, d))
    if chess_pieces.get(key):
        chess_pieces[key].append(i)
    else:
        chess_pieces[key] = [i]

# # 1000라운드까지만 가능
def start_game():
    round = 0
    while round < 1000:
        round += 1
        for i in range(K):
            key, d = pieces_position[i]
            x, y = key
            dx, dy = direction[d]
            dx += x                    
            dy += y
            piece_idx = [idx for idx, v in enumerate(chess_pieces[key]) if i == v][0] # 좌표값에 해당하는 리스트에서 체스말의 위치
            chess_pieces[key], pieces_list = chess_pieces[key][:piece_idx], chess_pieces[key][piece_idx:] # 좌표값에 해당하는 리스트에서 안 얹어진 체스말들 & 얹어진 체스말들로 구분
            ## 체스판에서 벗어나거나 파란색 칸을 밟을 경우
            if (N <= dx or dx < 0 or N <= dy or dy < 0) or grid[dx][dy] == 2:
                d = d_change[d]         # 방향 전환
                dx, dy = direction[d]
                dx += x
                dy += y
                ## 방향을 바꾼 후에도 체스판에서 벗어나거나 파란색 칸을 밟을 경우
                if (N <= dx or dx < 0 or N <= dy or dy < 0) or grid[dx][dy] == 2:
                    dx, dy = x, y       # 기존 좌표에 그대로 위치
                elif grid[dx][dy] == 1: # 빨간색 칸일 경우 얹어진 말들 순서 뒤집기
                    pieces_list = pieces_list[::-1] 
            elif grid[dx][dy] == 1:     # 빨간색 칸일 경우 얹어진 말들 순서 뒤집기
                pieces_list = pieces_list[::-1]
            
            new_key = (dx,dy)                             # 이동할 좌표
            if chess_pieces.get(new_key):                 # 이동할 좌표에 이미 체스말이 존재할 경우
                chess_pieces[new_key].extend(pieces_list) # 얹어!
                if len(chess_pieces[new_key]) >= 4:       # 얹고나서 체스말이 4개 이상일 경우 게임 종료
                    # for a in range(N):
                    #     for b in range(N):
                    #         print(chess_pieces[(a,b)], end=" ") if chess_pieces.get((a,b)) else print(0, end=" ")
                    #     print()
                    return round
            else:                                         # 이동할 좌표에 체스말이 없을 경우
                chess_pieces[new_key] = pieces_list       # 이동

            ## 함께 이동한 체스말들 좌표 변경
            for v in pieces_list:                   
                _, di = pieces_position[v]
                pieces_position[v] = (new_key, d) if v == i else (new_key, di) # 방향은 이동한 말들 중 가장 밑에 있던 말만 변경
            if not chess_pieces[key]:                     # 이동 후 해당 좌표에 말들이 없을 경우 좌표 제거
                del chess_pieces[key]
        # print(f"===========================|| round : {round} ||===========================") # 각 라운드 마다의 체스판 출력
        # for a in range(N):
        #     for b in range(N):
        #         print(chess_pieces[(a,b)], end=" ") if chess_pieces.get((a,b)) else print(0, end=" ")
        #     print()
        # print()
    return -1

print(start_game())