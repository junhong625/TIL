import sys

input = sys.stdin.readline

commands = {"L": [-1, 0], "R": [1, 0], "B": [0, -1], "T": [0, 1], "RT": [1, 1], "LT": [-1, 1], "RB": [1, -1], "LB": [-1, -1]}
def check(coordinate):
    x, y = coordinate
    return True if 1 <= x <= 8 and 1 <= y <= 8 else False

def move(coordinate, command):
    x, y = coordinate[0], coordinate[1]
    dx, dy = commands[command]
    return [dx+x, dy+y]
    
king, stone, cnt = map(str, input().split())
king = [ord(king[0])-64, int(king[1])]
stone = [ord(stone[0])-64, int(stone[1])]

for _ in range(int(cnt)):
    command = input().rstrip()
    if check(move(king, command)):
        if move(king, command) == stone:
            if check(move(stone, command)):
                stone = move(stone, command)
                king = move(king, command)
        else:
            king = move(king, command)

print(chr(king[0]+64)+str(king[1]))
print(chr(stone[0]+64)+str(stone[1]))