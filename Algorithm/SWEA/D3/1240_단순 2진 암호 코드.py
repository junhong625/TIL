def find_code(sub_arr, idx = 0):                                            # 패턴을 통해 코드를 찾는 함수
    total = 0               
    while idx <= M - 55:                                                    # 최소 길이가 56이여야 하기에 idx를 가로 길이-55까지 반복
        password = []                                                       # 암호코드가 들어갈 리스트
        for i in range(8):                                                  # 7자리씩 8개의 코드이기에 8번 반복
            if sub_arr[idx+i*7:idx+(i*7+7)] in pattern:                     # 해당 코드가 패턴에 존재하는 코드일 경우
                total += pattern[sub_arr[idx+i*7:idx+(i*7+7)]]              # total에 해당 코드 값
                password.append(pattern[sub_arr[idx+i*7:idx+(i*7+7)]])      # 암호코드 값 추가
            else:                                                           # 패턴이 존재하지 않는 코드일 경우
                total = 0                                                   # total 초기화하고 탐색 종료
                break
        if total and (sum(password[::2])*3 + sum(password[1::2])) % 10 == 0:# total이 0이 아니고 (홀수 자리의 합 x 3) + (짝수 자리의 합)이 10의 배수일 경우
            return total                                                    # total값 반환
        idx += 1
    return 0                                                            # 중간에 탈출하지 않았다면 0 반환

T = int(input())

pattern = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input().split())) for _ in range(N)]
    for row in arr:                     # arr의 각 row를 순회
        result = find_code(str(row))    # result에 코드 탐색 결과 할당
        if result:                      # result가 0이 아닐 경우 result 값 출력하고 탐색 종료
            print(f'#{t} {result}')
            break
    else:                               # 암호 코드가 없을 경우 0을 출력
        print(f'#{t} 0')