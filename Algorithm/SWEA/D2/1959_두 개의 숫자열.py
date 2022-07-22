T =int(input())
for i in range(1, T+1):
    max_sum = 0
    M, N = map(int, input().split())
    M_list = input().split()
    N_list = input().split()
    s = M_list if M < N else N_list
    b = M_list if M > N else N_list
    for j in range(abs(M-N)+1):
        total = 0
        for k in range(len(s)):
            total += int(s[k]) * int(b[k+j])
        if total > max_sum:
            max_sum = total
    print("#%d %d" %(i, max_sum))