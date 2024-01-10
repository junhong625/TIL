# 문제: 입력문자 위치를 변경하여 팰린드롬 구현하기

# 조건: 1) 1 <= 입력문자 <= 50
#      2) 입력문자는 모두 대문자
#      3) 정답이 없을 경우 "I'm Sorry Hansoo"
#      4) 정답이 여러개일 경우 사전순 우선순위 정답 출력

# 풀이: 입력문자의 반복횟수가 홀수를 가지는 문자가 1개를 초과해서는 안됨

# 방법: 1) 각 입력문자들의 개수 카운팅
#      2) 카운팅한 딕셔너리를 사전순으로 순회하며 문자 개수가 홀수일 때 중간 변수에 해당 문자 저장
#      3) 중간 문자열이 존재하는데 또 홀수 개수인 문자가 발견될 경우 "I'm Sorry Hansoo" 출력
#      4) 순회하면서 문자의 개수를 2로 나눈 수만큼 문자를 변수에 저장
#      5) 문자를 저장한 변수 + 중간 변수 + 문자를 저장한 변수를 뒤집은 문자

import sys

input = sys.stdin.readline

alphabet = {}

# 방법 1
for c in input().rstrip():
    alphabet.setdefault(c, 0)
    alphabet[c] += 1

center = ""
palindrome = ""
for c in sorted(alphabet.keys()):
    # 방법 2
    if alphabet[c] % 2:
        if not center:
            center = c
        # 방법 3
        else:
            print("I'm Sorry Hansoo")
            exit()
    # 방법 4
    palindrome += alphabet[c] // 2 * c    

# 방법 5
print(palindrome + center + palindrome[::-1])`