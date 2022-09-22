import sys, collections, time

sys.stdin = open('hws/algorithm/0922/input.txt', 'r')

def baby_gin(arr):
    for i in set(arr):
        if arr.count(i) >= 3 or (i+1 in arr and i+2 in arr):
            return True
    return False
    

T = int(input())
start = time.time()
for t in range(1, T+1):
    cards = list(map(int, input().split()))
    ## 앞에서부터 baby_gin 확인
    player1 = []
    player2 = []
    cards = collections.deque(cards)
    while cards:
        player1.append(cards.popleft())
        if baby_gin(player1):
            print(f'#{t} 1')
            break
        player2.append(cards.popleft())
        if baby_gin(player2):
            print(f'#{t} 2')
            break
    else:
        print(f'#{t} 0')

    ## 뒤에서부터 baby_gin 확인
    # player1 = cards[::2]
    # player2 = cards[1::2]

    # for i in range(6):
    #     result1 = baby_gin(player1)
    #     result2 = baby_gin(player2)
    #     if i == 5 and not result1 and not result2:
    #         print(f'#{t} 0')
    #         break
    #     player1.pop()  
    #     player2.pop()  
    #     if result1 and result2:
    #         if not baby_gin(player1) and not baby_gin(player2):
    #             print(f'#{t} 1')
    #             break
    #     elif result1 and not result2:
    #         print(f'#{t} 1')
    #         break
    #     elif not result1 and result2:
    #         print(f'#{t} 2')
    #         break
    # else:
    #     print(f'#{t} 0')
end = time.time()
print(f'#{end-start:.5f} sec')