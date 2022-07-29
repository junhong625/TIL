import copy
M = int(input())
N = copy.deepcopy(M)
count = 0
def add_cycle(N, count):
    if N < 10:
        N = int(str(N) * 2)
        count += 1
    else:    
        add = 0
        for n in str(N):
            add += int(n)
        N = int(str(N)[-1] + str(add)[-1])
        count += 1
    if M == N:
        return count
    return add_cycle(N, count)
print(add_cycle(N, count))