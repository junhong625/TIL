import sys

sys.stdin = open('TIL/Algorithm/SWEA/D5/input.txt', 'r')

## 암호코드를 찾아주는 함수
def find_code(row, idx=0): 
    binary = ''
    for num in row: # row를 16진수 2진수로 변환
        binary += change_binary(num)
    
    total_code = [] # 암호코드와 총합이 들어갈 리스트

    while idx <= len(binary)-56+1:                  # binary 최대 탐색 가능한 곳까지 탐색
        for i in range((len(binary)-idx)//56+1):    # 인덱스부터 binary끝까지의 길이를 구해 최대 두께만큼 순회
            code = []                               
            for p in range(8):                      # 암호 코드의 길이만큼 순회
                if binary[idx+p*7*i:idx+(p+1)*7*i] in pattern:  # 암호 코드의 두께 * 7만큼 슬라이싱 하며 탐색하여 존재하는 pattern일 경우
                    code.append(pattern[binary[idx+p*7*i:idx+(p+1)*7*i]]) # code에 패턴을 암호로 변화한 값을 추가
                else:                               # 없는 패턴일 경우 종료하고 다음 두께 탐색
                    break
            if len(code) == 8 and (sum(code[::2])*3 + sum(code[1::2])) % 10 == 0:   # 코드의 길이가 8자리이며 조건에 충족할 경우
                total_code.append([sum(code), code])                                # total_code에 암호 코드의 총합과 코드 추가
                break                                                               # 암호를 찾았으니 다음 idx부터 빠르게 탐색하기 위하여 종료
        idx += 1
    return total_code 

## pattern을 생성해주는 함수
def make_pattern():
    new_pattern = {}
    for p in range(1, M*4//56+1): 
        for key, value in base_pattern.items():
            new_pattern["".join([k*p for k in key])] = value
    return new_pattern

## 16진수를 2진수로 변환해주는 함수
def change_binary(num):
    b = ''
    num = int(num) if num.isdigit() else ord(num) - 55
    for _ in range(4):
        b = str(num % 2) + b
        num //= 2
    return b

T = int(input())

base_pattern = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}

for t in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    dup_row = {} # 똑같은 row일 경우 생략하기 위함
    dup_code = {}   # 똑같은 code일 경우 생략하기 위함
    result = 0
    pattern = make_pattern()
    print(M*4//56)
    for row in arr:
        if str(row) not in dup_row:  # 똑같은 row가 아닐 경우 
            total_code = find_code(row) # row에서 암호 코드를 찾고 결과값 total_code에 할당
            for total, code in total_code:  # total_code에서 하나씩 꺼내 순회
                if str(code) not in dup_code: # 중복되는 암호 코드가 아닐 경우
                    result += total         # result에 total을 추가
                    dup_code[str(code)] = 1 # dup_code에 추가
            dup_row[str(row)] = 1        # dup_row에 추가

    print(f'#{t} {result}')