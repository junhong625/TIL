import sys
from collections import deque 

N_list = deque([n for n in range(1, int(sys.stdin.readline())+1)])

while len(N_list) != 1:
    N_list.popleft()
    N_list.append(N_list.popleft())
print(N_list[0])

