import sys
input = sys.stdin.readline

N, M =map(int,input().split())
temp = list(map(int,input().split()))

result = [0] * (N+1)

for i in range(N):
    result[i+1] = result[i] + temp[i]
    
for _ in range(M):
    i , j = map(int,input().split())
    print(result[j] - result[i-1])