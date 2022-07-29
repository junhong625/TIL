h, m = map(int, input().split())
cooking = int(input())
if m+cooking >= 60:
    if h+((m+cooking)//60) >= 24:
        print(h+((m+cooking)//60)-24, (m+cooking)%60)
    else:
        print(h+((m+cooking)//60), (m+cooking)%60)
else:
    print(h, m+cooking)