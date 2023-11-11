import sys

input = sys.stdin.readline

N, R1, C1, R2, C2 = map(int, input().split())

alphabet = [chr(ord("a")+i) for i in range(N)]
dia = 2*N-1
for i in range(R1, R2+1):
    for j in range(C1, C2+1):
        i %= dia
        j %= dia
        dis = abs(N-1-i) + abs(N-1-j)
        if dis >  N-1:
            print(".", end="")
        else:
            print(alphabet[dis%26], end="")
    print()


