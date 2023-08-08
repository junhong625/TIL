number = "10034"
answer = 0
flag = False
target = ""
for i in range(len(number)):
    if flag:
        flag = False
        continue
    num = int(number[i])
    answer += 1
    target += str(num)
    if num == 0:
        continue
    if i < len(number):
        
        num += 1
        target += str(num)
        if number.startswith(target):
            flag = True
        else:
            answer += 1
            target = target[0:i+1]

print(answer, target)