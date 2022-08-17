# Algorithm_6💡

# DFS(깊이우선탐색)

> 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회 방법
> 
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 DFS를 반복해야 하므로 LIFO 구조의 스택 사용

## DFS 작동 구조

1.  시작 정점 v를 결정하여 방문
2.  정점 v에 인접한 정점 중에서
    
    1) 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문, 그리고 w를 v로 하여 다시 2.를 반복
    
    2) 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2를 반복
    
3. 스택이 공백이 될 때까지 2를 반복

### 일반적인 구현 방법

```python
adjList = [[1, 2],
           [0, 3, 4],
           [0, 4],
           [1, 5],
           [1, 2, 5],
           [3, 4, 6],
           [5]]

def DFS(v, N):
    visited = [0] * N   # visited 생성
    stack = [0] * N     # stack 생성
    top = -1
    print(v)
    visited[v] = 1
    while True:
        for w in adjList[v]:        # v의 인접 정점이 있는지 확인
            if visited[w] == 0:     # 방문한 적이 없는 경우
                top += 1            # push(v)
                stack[top] = v
                v = w               # 정해진 기준에 의해 v를 w로 이동
                visited[w] = 1      # 방문했던 것으로 변경
                print(v)
                break
        else:
            if top != -1:
                v = stack[top]      # pop(v)
                top -= 1
            else:
                break
    print(stack)
```

### 재귀로 구현

```python
# adjList 생성
V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input.split())
    adjList[a].append(b)
    adjList[b].append(a)

def DFS(v): # 재귀 함수
    print(v)
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:
            DFS(w)

visited = [0] * 7   # visited 생성
stack = [0] * 7     # stack 생성

DFS(1)
```