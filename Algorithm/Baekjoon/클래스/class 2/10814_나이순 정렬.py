import sys

N = int(sys.stdin.readline())

members = {}

for i in range(N): # 가입 순으로 저장
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    if age in members:
        members[age].append(name)
    else:
        members[age] = [name]

for key in sorted(members.keys()): # 나이 순으로 정렬하여 해당 나이의 가입자들을 출력
    for name in members[key]:
        print(f'{key} {name}')