T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    
    dp =[[0] * (n+1) for i in range(k+1)]

    for j in range(n+1):
        dp[0][j] = j
        
    for i in range(1,k+1):
        for j in range(1,n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
    print(dp[i][j])