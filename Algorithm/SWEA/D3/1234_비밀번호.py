for t in range(1, 11): 
    N, nums = map(str, input().split())
    password = []                               # 스택 구조
    for num in nums:
        if password and password[-1] == num:    # 중복될 경우 삭제
            password.pop()
            continue
        password.append(num)
    print(f'#{t} {"".join(password)}')    