for t in range(1, 11):
    N = int(input())
    adjList = [[] for _ in range(N+1)]
    tree = [0 for _ in range(N+1)]
    
    for _ in range(N):
        thing = list(map(str, input().split()))
        idx = int(thing.pop(0))
        tree[idx] = thing.pop(0)
        while thing: # 자식 노드들이 존재할 경우 인접 리스트에 할당
            adjList[idx].append(int(thing.pop(0)))
    
    while N != 0: # 연산자가 들어있는 노드가 나타날 때마다 자식 노드들을 연산자에 맞춰 계산한 값을 해당 노드에 할당
        if tree[N] == '+':
            tree[N] = int(tree[adjList[N][0]]) + int(tree[adjList[N][1]])
        if tree[N] == '-':
            tree[N] = int(tree[adjList[N][0]]) - int(tree[adjList[N][1]])
        if tree[N] == '*':
            tree[N] = int(tree[adjList[N][0]]) * int(tree[adjList[N][1]])
        if tree[N] == '/':
            tree[N] = int(tree[adjList[N][0]]) / int(tree[adjList[N][1]])
        N -= 1

    print(f'#{t} {int(tree[1])}')