import sys
from itertools import permutations 

## arr이 가능한 경우의 수인지 판단(이중포문을 통해 기준이 되는 숫자와 다른 숫자들을 비교)
# 불가능한 경우 : 기준이 되는 숫자(arr[i])보다 작은 숫자들이 오름차순으로 정렬되어 있는 경우
def check(arr):
    for i in range(len(arr)):
        cur = arr[i]
        flag = False
        for j in range(i+1, len(arr)):
            if flag and cur < arr[j] < arr[i]:
                return False
            if arr[i] > arr[j]:
                cur = arr[j]
                flag = True
    return True

input = sys.stdin.readline

n = int(input())

result = list(permutations(range(1,n+1), n))

for arr in result:
    if check(arr):    
        print(*arr)

