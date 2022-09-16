def bst(cur_node=1): # binary_search_tree, 이진트리는 중위 순회로 탐색하면 오름차순으로 조회 가능
    if cur_node > N: # N을 넘어갈 경우 종료
        return

    global num 
    
    bst(cur_node*2) # 
    tree[cur_node] = num
    num += 1
    bst(cur_node*2+1)

T = int(input())

for t in range(1, T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    num = 1
    bst()
    print(f'#{t} {tree[1]} {tree[N//2]}')