import sys

for _ in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    arr = [[i for i in range(b+1)] for _ in range(a+1)]
    for i in range(1, a+1):
        for j in range(b+1):
            arr[i][j] = sum(arr[i-1][:j+1])
    print(arr[i][j])