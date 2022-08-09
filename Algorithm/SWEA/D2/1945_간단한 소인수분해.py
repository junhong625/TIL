T = int(input())

for t in range(1, T+1):
    num = int(input()) # 소인수 분해 대상
    prime = [2,3,5,7,11]
    prime_list = [0] * 5
    idx = 0
    while num != 1:
        if num % prime[idx] == 0:
            prime_list[idx] += 1
            num //= prime[idx]
        else:
            idx += 1
    print(f'#{t}', end=' ')
    for i in prime_list:
        print(i, end=' ')
    print()

# num이 1이 될 때까지 prime으로 계산하며 소인수 분해하는 식
# 
# def next_prime(prime): # 다음 prime을 찾아내는 함수
#     while True:
#         prime += 1
#         for i in range(2, prime):
#             if prime % i == 0:
#                 break
#         else:
#             return prime

# for t in range(1, T+1):
#     num = int(input())
#     prime = 2
#     prime_list = {}
#     while num != 1:
#         if num % prime == 0:
#             if prime not in prime_list:
#                 prime_list[prime] = 1
#             else:
#                 prime_list[prime] += 1
#             num //= prime
#         else:
#             if prime not in prime_list:
#                 prime_list[prime] = 0
#             prime = next_prime(prime)
#     print(f'#{t} {prime_list}')
