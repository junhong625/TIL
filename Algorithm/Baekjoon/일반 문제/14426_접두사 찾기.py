import sys

input = sys.stdin.readline

N, M = map(int, input().split())

def check(N, M):
    words = {}

    for _ in range(N):
        word = input().rstrip()
        dummy = words
        for char in word:
            if dummy.get(char):
                dummy = dummy[char]
            else:
                dummy[char] = {"is" : True}
                dummy = dummy[char]

    ans = 0
    for _ in range(M):
        word = input().rstrip()
        dummy = words
        for idx, char in enumerate(word):
            if dummy.get(char):
                dummy = dummy[char]
            else:
                break
        else:
            ans += 1

    print(ans)
check(N, M)