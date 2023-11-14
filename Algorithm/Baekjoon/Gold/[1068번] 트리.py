# 문제: 특정 노드를 제거한 이후의 리프 노드 개수

# 조건: 1) 1 <= N <= 50

# 방법: 1) 노드 리스트를 만들어서 부모 노드 idx에 자식 노드 idx 넣기
#      2) 노드 리스트 순회하면서 제거할 노드 제거
#      3) bfs를 통해 리프 노드에 도달했을 때마다 cnt + 1


import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

nodes = [[] for _ in range(N)]
root = 0

# 방법 1
for idx, parent in enumerate(list(map(int ,input().split()))):
    if parent == -1:
        root = idx
        continue
    nodes[parent].append(idx)

# 방법 2
std = int(input()) # 제거할 노드
for node in nodes:
    if std in node:
        node.remove(std)

# 방법 3
q = deque([root])
cnt = 0

while q:
    node = q.popleft()

    if not nodes[node]:
        cnt += 1
        continue
    
    for next_node in nodes[node]:
        # print('%d -> %d', (node, next_node))
        q.append(next_node)

print(cnt)