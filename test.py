## pivot
def partition(l, r):                
    pivot = A[l]                        # 기준이 될 pivot 값 
    i, j = l, r                         # 왼쪽 끝 l과 오른쪽 끝 r을 i와 j에 저장
    while i <= j:                       # i와 j가 교차될 때 까지 반복
        while i <= j and A[i] <= pivot: # i와 j가 교차 되지 않았고 A[i]의 값이 pivot보다 작을 경우 큰 값을 찾기 위해
            i += 1                      # 오른쪽으로 이동
        while i <= j and A[j] >= pivot: # i와 j가 교차 되지 않았고 A[j]의 값이 pivot보다 클 경우 작은 값을 찾기 위해
            j -= 1                      # 왼쪽으로 이동
        if i < j:                       # pivot보다 큰 값이 왼쪽에 있고 작은 값이 오른쪽에 있으면
            A[i], A[j] = A[j], A[i]     # 서로 위치를 변경
    A[l], A[j] = A[j], A[l]             # 모든 정렬 작업이 끝난 후 pivot을 본인의 크기 순번인 j로 이동 
    return j

