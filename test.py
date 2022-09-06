import math
# 각도 계산하는 두 좌표의 각도를 계산하는 식
def check_angle(start, target):# start = 흰공, target = 목표 좌표
    a = target[0] - start[0]
    b = target[1] - start[1]

    angle = math.degrees(math.atan2(a, b))
    if angle < 0:
        return 360 + angle
    else:
        return angle

# 연장선을 그어서 좌표를 구하는 식
def new_xy(start, target): # start = hole, target = 목표구
    a = target[0] - start[0]
    b = target[1] - start[1]
    c = (a**2 + b**2) ** (1/2)

    c2 = c+5.73 # 연장된 빗변의 길이
    a2 = c2 * a / c
    b2 = c2 * b / c

    result = [0,0]
    result[0] = a2 if a2 >= 0 else  254 + a2
    result[1] = b2 if b2 >= 0 else  127 + b2
    return result
        

# 가장 치기 좋은 공 찾기(by 둔각)
# (나머지 두변의 합) / 수구와 홀간의 거리 식을 통해 나온 비율들을 각 타깃공마다 전체 홀의 값들을 가져와 가장 넣기 쉬운 공을 판단
def best_target_ball(s): # s: 수구
    angles = []
    for t in t_ball:
        sub = []
        for h in hole:
            a = (abs(h[0]-s[0])**2 + abs(h[1]-s[1])**2) ** (1/2)
            b = (abs(h[0]-t[0])**2 + abs(h[1]-t[1])**2) ** (1/2)
            c = (abs(t[0]-s[0])**2 + abs(t[1]-s[1])**2) ** (1/2)
            sub.append([(b+c)/a, t, h]) 
        angles.append(min(sub))
    return min(angles)

ball = [127, 63.5]
t_ball = [[70, 63.5+31.75], [63.5, 63.5+31.75]]
hole = [[0,127],[127,127],[254, 127],[0,0],[127,0],[254,0]]

# _, target_ball, hole = best_target_ball(ball)
# new = new_xy(hole, target_ball)
# print(check_angle(ball, new))

for h in hole:
    print(check_angle(ball, h))

print(18**(1/2))
