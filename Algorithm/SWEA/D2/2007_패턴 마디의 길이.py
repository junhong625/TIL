T = int(input())

# T만큼 반복하는 반복문
for t in range(1, T+1):
    patterns = input()
    check_word = ""
    # 입력 받은 문자열을 하나씩 잘라서 그 문자열의 길이만큼 다음 문자열과 비교하여 서로 같은지 판단하는 반복문
    for idx, char in enumerate(patterns):
        check_word += char
        if check_word == patterns[idx+1:idx+len(check_word)+1]:
            break
    print(f'#{t} {len(check_word)}')