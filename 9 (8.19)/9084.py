import sys
input = sys.stdin.readline

case = int(input().rstrip())
for i in range(case):
    N = int(input().rstrip())
    
    coins = list(map(int,input().split()))
    value = int(input().rstrip())
    dp = [0]*(value+1)
    dp[0] = 1
    for coin in coins:
        for k in range(value,-1,-1):
            j = 1
            while k-j*coin>=0:

                dp[k]  += dp[k-j*coin]
                j+=1
    print(dp[value])
