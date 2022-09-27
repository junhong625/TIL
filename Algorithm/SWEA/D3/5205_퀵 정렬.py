## 퀵 정렬 함수
def q_sort(l, r):                               # l: 탐색할 배열의 가장 왼쪽 idx, r: 탐색할 배열의 가장 오른쪽 idx
    pivot = nums[l]                             # 퀵 정렬 기준점
    i, j = l, r                                 # l과 r을 각각 i와 j에 할당
    while i <= j:                               # i와 j가 교차되기 전까지 반복
        while i <= j and pivot >= nums[i]:      # i와 j가 교차되기 전까지 i가 pivot보다 작은지 확인하면서 i를 이동
            i += 1
        while i <= j and pivot <= nums[j]:      # i와 j가 교차되기 전까지 j가 pivot보다 작은지 확인하면서 j를 이동
            j -= 1
        if i < j:                               # i와 j가 이동이 끝난 후 i와 j가 교차되지 않았다는 것은 
            nums[i], nums[j] = nums[j], nums[i] # i위치에 pivot보다 큰 값이, j위치에는 pivot보다 작은 값이 있다는 의미니까 서로 교환이 필요
    nums[l], nums[j] = nums[j], nums[l]         # 정렬이 끝난 후 pivot의 위치인 l과 j에 위치한 각 원소들을 교환(j의 위치가 l에 위치한 원소가 이동해야 할 위치) 
    return j

T = int(input())

for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = 0
    l, r = 0, N-1
    while result != N // 2:                     # 정렬이 끝난 원소의 위치가 N//2에 해당할 경우까지 반복
        result = q_sort(l, r)
        if result > N//2:                       # result의 값이 N//2보다 클 경우
            r = result-1                        # result보다 작은 idx 값들에 대한 정렬이 필요
        elif result < N // 2:                   # result의 값이 N//2보다 작을 경우
            l = result+1                        # result보다 큰 idx 값들에 대한 정렬이 필요
    print(f'#{t} {nums[result]}')

