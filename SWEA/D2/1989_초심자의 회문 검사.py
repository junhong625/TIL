T = int(input())
word_list=[]
for i in range(1,T+1):
    word = input()
    if len(word) % 2 == 0:
        if word[:len(word)//2] == word[:len(word)//2-1:-1]:
            print('#%d 1'% i)
        else:
            print('#%d 0'% i)
    else:
        if word[:len(word)//2+1] == word[:len(word)//2-1:-1]:
            print('#%d 1'% i)
        else:
            print('#%d 0'% i)