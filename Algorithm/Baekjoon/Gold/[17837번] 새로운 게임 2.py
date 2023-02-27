import sys

input = sys.stdin.readline

N, K = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
chess_pieces = {}
pieces_position = []
direction = [(), (0,1), (0,-1), (-1,0), (1,0)]
d_change = {1:2, 2:1, 3:4, 4:3}

## 말들의 좌표가 겹칠 경우 링크드 리스트 형식으로 체스 말들을 삽입 
# i: 순서, d: 방향
for i in range(K):
    x, y, d= map(int, input().split())
    key = x-1, y-1
    pieces_position.append((key, d))
    if chess_pieces.get(key):
        chess_pieces[key].append(i)
    else:
        chess_pieces[key] = [i]

print(chess_pieces)

# # 1000라운드까지만 가능
# (좌표: 체스말) 리스트를 각 좌표의 첫번째 원소의 순서에 맞게 정렬
def start_game():
    round = 0
    while round < 1000:
        round += 1
        print(round)
        print(chess_pieces)
        for i in range(N):
            key, d = pieces_position[i]
            x, y = key
            dx, dy = direction[d]       # 체스말 이동 좌표
            dx += x                    
            dy += y
            piece_idx = [idx for idx, v in enumerate(chess_pieces[key]) if i == v][0]
            chess_pieces[key], pieces_list = chess_pieces[key][:piece_idx], chess_pieces[key][piece_idx:]
            ## 체스판에서 벗어나거나 파란색 칸을 밟을 경우
            if (N <= dx or dx < 0 or N <= dy or dy < 0) or grid[dx][dy] == 2:
                pieces_position[i][1] = d_change[pieces_position[i][1]]
                dx, dy = direction[d]
                dx += x
                dy += y
                ## 방향을 바꾼 후에도 체스판에서 벗어나거나 파란색 칸을 밟을 경우
                if (N <= dx or dx < 0 or N <= dy or dy < 0) or grid[dx][dy] == 2:
                    dx, dy = x, y
                elif grid[dx][dy] == 1:
                    pieces_list = pieces_list[::] 
            elif grid[dx][dy] == 1:
                pieces_list = pieces_list[::]
            
            new_key = (dx,dy)
            if chess_pieces.get(new_key):
                chess_pieces[new_key].extend(pieces_list)
                # if len(chess_pieces[new_key]) >= 4:
                #     return round
            else:
                chess_pieces[new_key] = pieces_list
    return -1

print(start_game())