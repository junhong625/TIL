def min_binary_heap(num): # 최소힙의 새로운 노드에 숫자를 삽입하는 함수
    global last
    last += 1                                       # 새로운 숫자가 들어갈 노드
    binary_heap[last] = num                                # 노드에 숫자 삽입
    c = last                                        # 자식 노드
    p = c//2                                        # 부모 노드
    while p != 0:                                   # 부모 노드가 0이 되면 종료
        if binary_heap[c] < binary_heap[p]:                       # 자식 노드가 부모 노드보다 작을 경우 -> 최소힙 조건에 충족하지 않음
            binary_heap[c], binary_heap[p] = binary_heap[p], binary_heap[c]     # 자식 노드와 부모 노드의 값을 서로 교환
            c = p                                   # 자식 노드 새로 설정
            p = c // 2                              # 부모 노드 새로 설정
        else:
            break

T = int(input())

for t in range(1,T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    binary_heap = [0 for _ in range(N+1)]                  
    last, result = 0, 0

    for n in nums: # 새로운 숫자 삽입
        min_binary_heap(n)

    while last != 1: # 마지막 노드의 부모 노드들의 합을 계산
        result += binary_heap[last//2]
        last //= 2

    print(f'#{t} {result}')