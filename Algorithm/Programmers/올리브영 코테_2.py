kor = ["AAA", "BCD", "AAAAA", "ZY"]
usa = ["AB", "AA", "TTTT"]
incs = ["AB BCD AA AAA TTTT AAAAA", "BCD AAA", "AB AAA TTTT BCD", "AA AAAAA AB", "AAA AB BCD"]
from collections import defaultdict

counter = defaultdict(int)

for i in range(len(incs)):
    arr = sorted(incs[i].split(" "))
    for j in range(len(arr)-1):
        for k in range(j+1, len(arr)):
            if (arr[j] in kor and arr[k] in kor) or (arr[j] in usa and arr[k] in usa):
                continue
            key = f"{arr[j]} {arr[k]}"
            counter[key] = counter.get(key) + 1 if key in counter else 1

print(max(counter.values()))