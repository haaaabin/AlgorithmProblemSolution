import sys
input = sys.stdin.readline

n = int(input())

time = list(map(int,input().split()))

time.sort()

total = 0
for i in range(n+1):
    total += sum(time[:i])
    
print(total)