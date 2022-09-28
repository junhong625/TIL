# 서로소 집합(Disjoint-sets)

> 서로소 또는 상호 배타 집합들은 서로 중복 포함된 원소가 없는 집합(교집합 X)
> 
- 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분한다.
    - 이를 대표 원소(representative)라 한다.

## 상호 배타 집합을 표현하는 방법

### 1. 연결 리스트

- 같은 집합의 원소들은 하나의 연결리스트로 관리
- 연결리스트의 맨 앞의 원소를 집합의 대표 원소로 삼는다.
- 각 원소는 집합의 대표 원소를 가리키는 링크를 갖는다.

### 2. 트리

- 하나의 집합을 하나의 트리로 표현
- 자식 노드가 부모 노드를 가리키며 루트 노드가 대표 원소가 된다.

## 상호 배타 집합 연산

### 1. Make-Set(x)

- x가 대표 원소인 집합을 만들라는 의미
- 코드

```python
def makeSet(x):
	p[x] = x
```

### 2. Find-Set(x)

- x가 포함된 집합의 대표 원소를 출력하라는 의미
- 코드

```python
def findSet(x):
	while p[x] != x:
		x = p[x]
	return x
```

### 3. Union(x, y)

- x가 대표 원소인 집합과 y가 대표 원소인 집합을 합치라는 의미
- 앞에 위치한 인자를 대표 원소로 지정(x)
- 코드

```python
def union(x, y):
	p[findSet(y)] = findSet(x)
```

## 연산의 효율을 높이는 방법

### Rank를 이용한 Union

- 각 노드는 자신을 루트로 하는 subtree의 높이를 랭크(Rank)라는 이름으로 저장한다.
- 두 집합을 합칠 때 rank가 낮은 집합을 rank가 높은 집합에 붙인다.

### Path compression

- Find-Set을 행하는 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 포인터를 바꾸어 준다.

# KRUSKAL 알고리즘

> 간선을 하나씩 선택해서 MST를 찾는 알고리즘
> 
1. 최초, 모든 간선을 가중치에 따라 오름차순으로 정렬
2. 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킴
    1. 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택
3. n-1개의 간선이 선택될 때 까지 2를 반복

## Disjoint-sets를 사용한 풀이

```python
def find_set(x):                        # 대표 원소 탐색
    while rep[x] != x:
        x = rep[x]
    return x

def union(x, y):                        # 병합
    rep[find_set(y)] = find_set(x)

V, E = map(int, input().split())
edges = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append([u, v, w])
edges.sort(key=lambda x:x[2])
rep = [i for i in range(V+1)]           # 대표원소 배열

N = V + 1                               # 정점의 개수
cnt = 0                                 # 선택한 edge의 수
total = 0
for u, v, w in edges:
    if find_set(u) != find_set(v):      # 대표 원소가 다를 경우 카운트
        cnt += 1
        union(u, v)
        total += w
        if cnt == N - 1:
            break
print(total) 
``` 