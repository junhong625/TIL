import sys

while True:
    tri = list(map(int, sys.stdin.readline().split()))
    if sum(tri) == 0: # 삼각형의 합이 0일 경우 종료
        break
    tri.sort()  # 오름차순 정렬
    if tri[2]**2 == tri[0]**2 + tri[1]**2: # 피타고라스의 정리
        print('right')
    else:
        print('wrong')