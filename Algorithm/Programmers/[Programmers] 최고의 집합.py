def solution(n, s):
    if s < n:
        return [-1]
    answer = [s//n]*n
    for i in range(s-sum(answer)):
        answer[i] += 1
    
    return sorted(answer)