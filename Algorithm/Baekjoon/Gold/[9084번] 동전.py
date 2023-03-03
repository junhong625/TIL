import sys
from collections import deque
import datetime
input = sys.stdin.readline

def bfs(target):
    q = deque([target])
    cnt = 0
    idx = 0
    while q and idx < len(coins):
        print(q)
        t = q.popleft()
        if t <= 0:
            if t == 0: cnt += 1
            continue
        cost = coins[idx]
        for i in range(1, t//cost+1):
            q.append(t-cost*i) 
        idx += 1
    return cnt

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    print(bfs(target))
print(f'ab{a}')