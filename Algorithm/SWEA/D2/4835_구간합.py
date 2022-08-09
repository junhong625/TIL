def sum(array): # 배열의 모든 원소 합을 반환하는 함수
    total = 0
    for i in array:
        total += i
    return total

def min(*args): # 여러 개의 argument중 가장 작은 값을 반환하는 함수
    min_val = args[0]
    for i in args:
        min_val = min_val if i > min_val else i
    return min_val

def max(*args): # 여러 개의 argument중 가장 큰 값을 반환하는 함수
    max_val = args[0]
    for i in args:
        max_val = max_val if i < max_val else i
    return max_val

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split()) # 정수의 개수, 합을 계산해야 할 숫자 개수 
    arr = list(map(int, input().split())) # 정수가 들어있는 배열
    max_sum, min_sum = 0, sum(arr) # 최대값, 최소값이 들어가 변수
    for idx in range(N-M+1): # N에서 M을 뺀 수 보다 더 큰 수에서는 M만큼의 연속된 숫자 개수가 안 나오기에 그 전까지만 반복 
        dummy = 0 # 임시적으로 연속된 수의 합이 더해질 변수
        for j in range(M): # M만큼 반복하여 연속된 수를 모두 dummy에 더한 후 미리 생성해둔 max, min 함수를 이용해 최대값, 최소값과 비교
            dummy += arr[idx+j]
        max_sum = max(max_sum, dummy)
        min_sum = min(min_sum, dummy)
    print(f'#{t} {max_sum-min_sum}')
