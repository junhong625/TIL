T = int(input())
for i in range(1, T+1):
    raws, length = map(int, input().split())
    table = []
    total = 0
    for j in range(raws):
        raw = input().split()
        table.append(raw)
        count = 0
        for k in range(raws):
            if raw[k] == '1':
                count += 1
                if k == raws-1:
                    if count == length:
                        total += 1
            else:
                if count == length:
                    total += 1
                count = 0
    for l in range(raws):
        count = 0
        for m in range(raws):
            if table[m][l] == '1':
                count += 1
                if m == raws-1:
                    if count == length:
                        total += 1
            else:
                if count == length:
                    total += 1
                count = 0
    print("#%d %d" %(i, total))