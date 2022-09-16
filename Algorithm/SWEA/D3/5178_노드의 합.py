T = int(input())

for t in range(1, T+1):
    N, M, L = map(int, input().split())
    node_number = N//2*2 # 마지막 왼쪽 노드 번호 저장
    tree = [0 for _ in range(N+2)] # 트리 생성 -> 아래의 자식 노드들의 합을 구하는 부분에서 IndexError가 발생하는 부분을 방지해주기 위한 padding 
    
    for _ in range(M): # 리프 노드에 value 삽입
        node, value = map(int, input().split())
        tree[node] = value

    while node_number > 1: # 자식 노드들의 합을 부모 노드에 더해주는 반복문
        tree[node_number//2] = tree[node_number] + tree[node_number+1]
        node_number -= 2 # 자식 노드는 2개씩 주어지기에 -2를 해줘 다음으로 계산할 부모 노드의 왼쪽 자식 노드로 이동 

    print(f'#{t} {tree[L]}')