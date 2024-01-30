import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    coins = list(map(int,input().split()))
    coins.insert(0,0)
    amount = int(input())
    
    dp = [[0] *(amount+1) for i in range(n+1)]
    
    for i in range(n+1):
        #0원으로 만들 수 있는 가지 수는 1로 초기화
        dp[i][0] = 1
            
    for j in range(1,n+1):
        for i in range(1,amount+1):
            #앞선 coin의 가지수를 다음 coins 칸에 가지고 온다
            dp[j][i] = dp[j-1][i]
            #만들고 싶은 값에서 내가 지금 가진 동전을 뺀다.
            if i-coins[j] >= 0:
                dp[j][i] += dp[j][i-coins[j]]
    print(dp[n][amount])