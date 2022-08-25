import sys
from collections import deque
sys.stdin = open('TIL/Algorithm/Baekjoon/클래스/class 2/input.txt', 'r')

t = int(sys.stdin.readline())
deq = deque()

for _ in range(t):
    input = sys.stdin.readline()
    if 'push_back' in input:
        deq.append(input.split()[1])
    elif 'push_front' in input:
        deq.appendleft(input.split()[1])
    elif 'pop_front' in input:
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif 'pop_back' in input:
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif 'size' in input:
        print(len(deq))
    elif 'empty' in input:
        print(1 if not deq else 0)
    elif 'front' in input:
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif 'back' in input:
        if deq:
            print(deq[-1])
        else:
            print(-1)