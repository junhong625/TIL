num = {1:[1], 2:[2,4,8,6], 3:[3,9,7,1], 4:[4, 6], 5:[5], 6:[6], 7:[7,9,3,1], 8:[8,4,2,6], 9:[9,1], 0:[10]}
n = [1, 1, 4, 4, 2, 1, 1, 4, 4, 2]

a, b = map(int, input().split())
print(num[a%10][b%n[a%10]-1])