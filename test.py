arr = [1,2,3,4]
subsets = [[]]

for num in arr:
    for i in range(len(subsets)):
        subsets.append(subsets[i] + [num])

print(subsets)