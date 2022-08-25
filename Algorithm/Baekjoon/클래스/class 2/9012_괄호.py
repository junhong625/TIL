import sys

sys.stdin = open('TIL/Algorithm/Baekjoon/클래스/class 2/input.txt', 'r')

N = int(sys.stdin.readline())
for _ in range(N):
    bracket = list(map(str, sys.stdin.readline()))[:-1] # sys.stdin으로 받을 경우 개행을 \n으로 받아오기에 해당 부분 잘라내기위해 [:-1]로 슬라이싱
    stack = [] # 괄호를 하나씩 넣을 스택 구조
    for b in bracket:   # 괄호를 하나씩 순회
        if stack and stack[-1] + b == '()': # 스택에 괄호가 존재하고 스택의 마지막 괄호와 순회하는 괄호가 짝이 맞을 경우 스택의 마지막 괄호 삭제
            stack.pop()
        else:                               # 그렇지 않을 경우 괄호 삽입
            stack.append(b)
    if stack: # 남은 괄호가 있을 경우 
        print('NO')
    else:     # 남은 괄호가 없을 경우
        print('YES')            