import sys

T = int(sys.stdin.readline())

for _ in range(T): 
    M, N, K = map(int, sys.stdin.readline().split())
    k_cabbage = []
    cnt = 0
    for _ in range(K):
        k_cabbage.append(list(map(int, sys.stdin.readline().split())))
    while k_cabbage: # bfs 사용하여 풀기
        stack = []
        stack.append(k_cabbage.pop(0))
        while stack: 
            start = stack.pop()
            for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
                if k_cabbage and [dx+start[0], dy+start[1]] in k_cabbage:
                    stack.append([dx+start[0], dy+start[1]])
                    k_cabbage.remove([dx+start[0], dy+start[1]])
        cnt += 1
    print(cnt)
        
            
    
    
