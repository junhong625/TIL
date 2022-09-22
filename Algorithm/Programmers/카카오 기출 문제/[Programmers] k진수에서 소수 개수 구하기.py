def solution(n, k):
    def prime_num(num):
        for i in range(2, num):
            if nums[i] == True:
                for j in range(i*2, num+1, i):
                    nums[j] = False
        return nums[num]            
    nums = [False, False] + [True for _ in range(1, n+1)]

    s = ''
    while n != 0:
        s = str(n % k) + s
        n //= k
    s = s.split('0')

    answer = 0
    std = 0
    for i in s:
        if i.isdigit():
            if prime_num(int(i)):
                answer += 1
    return answer