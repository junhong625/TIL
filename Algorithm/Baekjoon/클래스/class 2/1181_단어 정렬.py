sort_words = {}

for i in range(int(input())):                   # 문자열 길이를 key로 가지고 문자열을 value로 가진 dict생성
    word = input()             
    if len(word) in sort_words:                     
        if word not in sort_words[len(word)]:
            sort_words[len(word)].append(word)
    else:
        sort_words[len(word)] = [word] 

for key in sorted(sort_words.keys()):           # 길이순으로 저장된 문자들을 사전 순으로 출력
    for word in sorted(sort_words[key]):
        print(word)