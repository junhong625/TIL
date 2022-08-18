x, y, w, h = map(int, input().split())

print(min(min(x, abs(w-x)), min(y, abs(h-y)))) # 최소값을 출력