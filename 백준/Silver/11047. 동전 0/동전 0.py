import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
  
cnt = 0
for i in range(n):
    cnt += k // coins[i]
    k = k % coins[i]
    
print(cnt)