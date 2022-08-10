from collections import Counter

word = input().upper()

counter = Counter(word)

duplicate = list(counter.values()).count(max(counter.values()))

print(max(counter, key=lambda x:counter[x]) if duplicate == 1 else '?')