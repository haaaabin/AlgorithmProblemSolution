import sys
input = sys.stdin.readline
K,N = map(int,input().split())
temp = [int(input()) for _ in range(K)]

start = 1
end = max(temp)

while start <= end:
    mid = (start + end) //2
    total = 0

    for i in temp:
        total += i // mid
    
    if total >= N:
        start = mid+ 1
    else:
        end = mid - 1

print(end)