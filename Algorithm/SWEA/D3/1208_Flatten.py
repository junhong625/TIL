def min_idx(arr): # 배열에서 가장 큰 값의 idx를 반환하는 함수
    idx = 0
    val = arr[0]
    for i in range(100):
        if arr[i] < val:
            val, idx = arr[i], i
    return idx

def max_idx(arr): # 배열에서 가장 작은 값의 idx를 반환하는 함수
    idx = 0
    val = arr[0]
    for i in range(100):
        if arr[i] > val:
            val, idx = arr[i], i
    return idx

for t in range(1, 11):
    limit = int(input()) # 작업 가능한 횟수
    arr = list(map(int, input().split())) # 상자가 들어있는 배열
    for _ in range(limit): # 작업 가능한 횟수만큼 반복 
        arr[max_idx(arr)] -= 1 # 가장 상자가 많이 쌓여있는 index에서 상자를 하나 빼서
        arr[min_idx(arr)] += 1 # 가장 상자가 적게 쌓여있는 index로 이동
    print(f'#{t} {arr[max_idx(arr)] - arr[min_idx(arr)]}') # 작업을 완료한 후 상자가 가장 많이 쌓여있는 곳과 가장 적게 쌓여있는 곳의 상자 높이 차이를 출력