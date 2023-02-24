import sys

input = sys.stdin.readline

N, K = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
chess_pieces = {}
direction = [(), (0,1), (0,-1), (-1,0), (1,0)]

for i in range(K):
    x, y, d= map(int, input().split())
    if chess_pieces.get((x,y)):
        chess_pieces[(x,y)].append((i,d))
    else:
        chess_pieces[(x,y)] = [(i,d)]

round = 0
while round < 1000:
    round += 1
    for i in sorted(list(chess_pieces.keys()), key=lambda x:chess_pieces[x][0][0])

    