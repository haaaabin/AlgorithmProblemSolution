import sys
input = sys.stdin.readline

n = int(input())

gamepan = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j ==n-1:
            break        
        
        #오른쪽으로 이동했을 때 해당 칸에 적힌 거리만큼 이동
        right = j + gamepan[i][j]
        if right < n:
            dp[i][right] += dp[i][j]

        #아래로 이동
        down = i + gamepan[i][j]
        if down < n:
            dp[down][j] += dp[i][j]
          
print(dp[-1][-1])   