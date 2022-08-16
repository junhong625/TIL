T = int(input())

def len(s): # 내장함수 len의 역할
    cnt = 0
    for i in s:
        cnt += 1
    return cnt

def replace(word, s1, s2): # str의 메서드 replace의 역할
    idx = 0
    while idx < len(word):
        if word[idx:idx+len(s1)] == s1:
            word = word[:idx] + s2 + word[idx+len(s1):]
        else:
            idx += 1
    return word
        

for t in range(1, T+1): 
    A, B = map(str, input().split())
    total = (len(A) - len(replace(A, B, ''))) // len(B) + len(replace(A, B, '')) # B에 해당하는 문자열을 제거한 후 그 없어진 문자열의 길이를 B로 나눈 몫과 남은 문자 배열의 길이 
    print(f'#{t} {total}')