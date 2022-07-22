from collections import Counter
 
def check_horizontal(line):
    result = Counter(line)
    for i in range(1, 10):
        if result[str(i)] != 1:
            return 0
    return 1
 
def check_vertical(line):
    for i in range(9):
        new_line = []
        for j in range(9):
            new_line.append(line[j][i])
        result = Counter(new_line)
        for k in range(1, 10):
            if result[str(k)] != 1:
                return 0
    return 1
 
def check_3to3(sdoku):
    for j in range(0, 9, 3):
        for k in range(0, 9, 3):
            line = []
            for l in range(3):
                for m in range(3):
                    line.append(sdoku[j+l][k+m])
            result = Counter(line)
            if check_horizontal(result) != 1:
                return 0
    return 1
 
T = int(input())
for i in range(1, T+1):
    sdoku = []
    result = 1
    for _ in range(9):
        line = input().split()
        if check_horizontal(line) != 1:
            result = 0
        sdoku.append(line)
    if check_vertical(sdoku) != 1:
        result = 0
    if check_3to3(sdoku) != 1:
        result = 0
    print("#%d %d" %(i, result))