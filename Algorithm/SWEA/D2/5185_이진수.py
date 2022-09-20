import sys

sys.stdin = open('TIL/Algorithm/SWEA/D2/input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, hex = map(str, input().split())
    binary = ''                                         # 이진수로 변환되어 할당될 변수
    for h in hex:                                       # 16진수 순회
        num = int(h) if h.isdigit() else ord(h) - 55    # 숫자가 아닐 경우 ASCII코드를 이용하여 숫자로 변경
        sub = ''                                        # 2진수로 변환한 4자리가 할당될 변수
        for _ in range(4):                              # 2진수 4자리의 값들 탐색
            sub = str(num % 2) + sub                    # num을 2로 나눈 나머지를 뒤쪽이 아닌 앞쪽에 추가
            num //= 2                                   # num을 2로 나눠줌
        binary += sub                                   # 2진수 4자리를 binary에 추가
    print(f'#{t} {binary}')
