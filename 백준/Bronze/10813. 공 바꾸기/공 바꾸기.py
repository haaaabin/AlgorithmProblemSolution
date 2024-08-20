n,m = map(int,input().split())
temp = [i+1 for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    temp1 = temp[a-1]
    temp[a-1] = temp[b-1]
    temp[b-1] = temp1

print(*temp)