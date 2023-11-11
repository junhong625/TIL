import sys

input = sys.stdin.readline

S = input().rstrip().replace(">", "<").split("<")
ans = ""

for i in range(len(S)):
    ans += f"<{S[i]}>" if i % 2 else " ".join([word[::-1] for word in S[i].split()])

print(ans)