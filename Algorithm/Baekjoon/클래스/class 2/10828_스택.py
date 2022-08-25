import sys

sys.stdin = open('TIL/Algorithm/Baekjoon/클래스/class 2/input.txt', 'r')

T = int(sys.stdin.readline())
stack = []

for _ in range(T):
    input = sys.stdin.readline()
    if input[:3] == 'pus': # push일 경우
        stack.append(int(input.split()[1]))
    elif input[:3] == 'top': # top일 경우
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif input[:3] == 'siz': # size일 경우
        print(len(stack))
    elif input[:3] == 'emp': # empty일 경우
        print(1 if not stack else 0)
    elif input[:3] == 'pop': # pop일 경우
        if stack:
            print(stack.pop())
        else:
            print(-1)