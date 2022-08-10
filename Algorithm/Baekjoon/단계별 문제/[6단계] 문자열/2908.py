A, B = map(str, input().split())

print(max(int(A[::-1]), int(B[::-1])))