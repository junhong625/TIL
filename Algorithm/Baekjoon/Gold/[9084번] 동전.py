import sys
input = sys.stdin.readline

def cal(target, coins):
    dp = [1] + [0 for _ in range(target)]
    for coin in coins:
        for i in range(coin, target+1):
            if i - coin >= 0:
                dp[i] += dp[i-coin]
    print(dp[target])
    
for _ in range(int(input().strip())):
    N = int(input().strip())
    coins = list(map(int, input().strip().split()))
    target = int(input().strip())
    cal(target, coins)