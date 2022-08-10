cro_alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for alp in cro_alp:
    if alp in word:
        word = word.replace(alp, ' ')

print(len(word))