A = int(input())

range_num, cur_num, cnt = 6, 1, 1
while A > cur_num:
    cur_num += range_num
    range_num += 6
    cnt += 1
# print(cur_num)

print(cnt)