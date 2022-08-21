def count(s, t):                        # 문자열s 에서 t의 개수를 반환
    cnt = 0
    for char in s:
        if char == t:
            cnt += 1
    return cnt

def check_magnetic(arr):                # 교착 상태 개수를 계산하는 함수
    total = 0
    for i in range(100):            
        mag_arr = ''                    # N과 S를 더할 문자열 (스택과 유사한 개념, pop보다는 strip 메서드를 이용하여 좌우를 편리하게 제거하고 문자열을 사용)
        for j in range(100):
            if arr[j][i] != 0:          # 0이 아닐 경우 문자열로 변환하여 더해줌 
                mag_arr += str(arr[j][i])
            
        mag_arr.lstrip('2').rstrip('1') # 왼쪽에서는 2를 오른쪽에서는 1을 제거 
        total += mag_arr.count('12')    # 12의 개수를 total에 더해주기 (ex : NNSNSS)
    return total

for t in range(1, 11):
    l = int(input())
    arr = [list(map(int, input().split())) for _ in range(l)]
    print(f'#{t} {check_magnetic(arr)}')