sound = {'12345678':'ascending', '87654321':'descending'}

s = input().replace(' ', '')

if s in sound:
    print(sound[s])
else:
    print('mixed')