import sys

N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num:
        stack.append(num)
    else:
        stack.pop()
print(sum(stack))