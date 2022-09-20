import sys

sys.stdin = open('TIL/Algorithm/SWEA/D2/input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = float(input())
    binary = ''                         # 2진수가 들어갈 변수
    while N != 0:                       # N이 0이 되면 종료
        if len(binary) >= 13: break     # 2진수의 길이가 13 이상이 될 경우 종료

        if N * 2 >= 1:                  # N * 2가 1이상일 경우
            binary += '1'               # 2진수에 1을 추가
            N = N * 2 - 1               # N을 변경
        else:                           # N * 2가 1미만일 경우
            binary += '0'               # 2진수에 0을 추가
            N = N * 2                   # N을 변경

    print(f'#{t} {binary if len(binary) < 13 else "overflow"}')
