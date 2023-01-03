import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x, y = 0, 0
    maxX, minX, maxY, minY = 0, 0, 0, 0
    dx, dy = 0, 1
    case = list(str(input()))
    while case:
        m = case.pop()
        
        # 기호에 따른 작업 정하기
        if m in ('F', 'B'):
            x, y = x+dx if m == 'F' else x-dx, y+dy if m == 'F' else y-dy
            if x > 0:
                maxX = max(maxX, x)
            elif x < 0:
                minX = min(minX, x)
            if y > 0:
                maxY = max(maxY, y)
            elif y < 0:
                minY = min(minY, y)
        else:
            if dy:
                if m == 'L':
                    dx, dy = -dy, dx
                else:
                    dx, dy = dy, dx
            else:
                if m == 'L':
                    dx, dy = dy, dx
                else:
                    dx, dy = dy, -dx
    print((maxX-minX)*(maxY-minY))

        # 0, 1 => L: -1, 0, R: 1, 0
        # 0, -1 => L: 1, 0, R:-1, 0
        # 1, 0 => L: 0, 1, R: 0, -1
        # -1, 0 => L: 0, -1, R: 0, 1