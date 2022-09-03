import sys

def z(arr):
    if len(arr) != 2:
        for i in range(0, len(arr), len(arr//2)):
            for j in range(0, len(arr), len(arr//2)):
                z([[x,y] for x in range(i, i+len(arr)//2) for y in range(j, j+len(arr)//2)])
    else:
        for i in range(2):
            for j in range():
                pass



N, r, c = map(int, sys.stdin.readline().split())

arr = [[0 for _ in range(2**N)] for _ in range(2**N)]
cnt = 0

