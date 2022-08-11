# X표시부터 거꾸로 올라가는 코드

def find_end(arr): # 2인 값의 좌표를 찾아내는 함수
    result = ()
    for i in range(100):
        if arr[99][i] == 2:
            result = i
    return result

delta = [[-1,0], [0,-1], [0,1]] # 위, 왼쪽, 오른쪽

for _ in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    y, x = 99, find_end(arr) # 문제에서 가로 좌표는 x, 세로 좌표는 y 
    direction = 0 # 방향
    while y != 0: # 세로 좌표가 0이 될 경우 종료

        if direction == 0: # 위로 올라가고 있을 경우
            if 0 <= y + delta[1][0] < 100 and 0 <= x + delta[1][1] < 100 and arr[y + delta[1][0]][x + delta[1][1]] == 1: # 왼쪽에 1이 있는지 체크 
                direction = 1
            elif 0 <= y + delta[2][0] < 100 and 0 <= x + delta[2][1] < 100 and arr[y + delta[2][0]][x + delta[2][1]] == 1: #오른쪽에 1이 있는지 체크
                direction = 2

        else: # 왼쪽이나 오른쪽으로 이동하고 있을 경우
            if not(0 <= y + delta[1][0] < 100 and 0 <= x + delta[1][1] < 100) or arr[y + delta[1][0]][x + delta[1][1]] != 1: # 왼쪽이 막혀있거나 0일 경우
                direction = 0 # 위로 이동
            elif not(0 <= y + delta[2][0] < 100 and 0 <= x + delta[2][1] < 100) or arr[y + delta[2][0]][x + delta[2][1]] != 1: # 오른쪽이 막혀있거나 0일 경우
                direction = 0 # 위로 이동
        
        # 정해진 방향대로 이동
        y += delta[direction][0] 
        x += delta[direction][1]

    print(f'#{T} {x}')
        
