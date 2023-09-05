# 조건 : 수빈이(N)이 동생(K)을 최대한 빨리 찾기
#       순간이동 : X*2
#       걷기 : X+1 or X-1
# 방법 : bfs를 이용하여 최단시간 찾기

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

def find(N, K):
    q = deque([N])
    visited = [0 for _ in range(100001)]

    while q:
        v = q.popleft()
        if v == K:
            return visited[v]
        for i in (v-1, v+1, v*2):
            if 0 <= i <= 100000 and not visited[i]:
                q.append(i)
                visited[i] = visited[v] + 1

print(find(N, K))