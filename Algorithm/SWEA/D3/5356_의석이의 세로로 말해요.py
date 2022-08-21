def len(s): # 내장함수 len
    cnt = 0
    for _ in s:
        cnt += 1
    return cnt

T = int(input())

for t in range(1, T+1):
    arr = [input() for _ in range(5)] # 배열 생성
    maxLen = 0                        # col의 기준이 될 단어들 중 최대 길이
    
    for word in arr:
        maxLen = maxLen if maxLen > len(word) else len(word)
    
    print(f'#{t}', end=' ')
    for i in range(maxLen):           # 세로로 출력
        for j in range(5):
            if len(arr[j]) > i:
                print(arr[j][i], end='')
    print()