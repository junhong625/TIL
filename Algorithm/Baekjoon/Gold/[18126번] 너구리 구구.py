import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

dist = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(N-1):
    a, b, c = list(map(int, input().split()))
    dist[a].append((b,c))
    dist[b].append((a,c))

def dajk(): # 다익스트라
    q = deque([(1, 0)])
    while q:
        cur, tot = q.popleft()
        for w,v in dist[cur]: # w: 이동 좌표, v: 가중치
            if not visited[w]: # w를 방문하지 않았을 경우
                visited[w] = tot+v # 가중치와 현재 값을 더한 이동 거리
                q.append((w, tot+v)) # q에 해당 좌표 추가
            else: # w를 방문했을 경우
                if visited[w] > tot+v: # 가중치와 현재 값을 더한 이동거리 visited[w]에 더한 값보다 클 경우에만
                    visited[w] = tot+v # 해당 수치 반영
                    q.append((w, tot+v)) # q에 해당 좌표 추가
    return max(visited)

print(dajk())