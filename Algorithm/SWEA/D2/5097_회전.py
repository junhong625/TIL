T = int(input())

# 일반 풀이
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     print(f'#{t} {arr[M%N]}')

# Queue를 이용한 풀이
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        arr.append(arr.pop(0)) # deQueue이후 바로 해당 데이터를 바로 enQueue
    print(f'#{t} {arr[0]}')