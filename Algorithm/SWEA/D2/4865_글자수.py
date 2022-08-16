T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2 = input()
    max_cnt = 0
    for char in str1: # str1의 문자들을 str2의 문자들과 비교하여 가장 많이 나오는 문자열 개수 파악
        cnt = 0
        for char2 in str2:
            if char == char2:
                cnt += 1 
        max_cnt = max_cnt if max_cnt > cnt else cnt
    print(f'#{t} {max_cnt}')
        