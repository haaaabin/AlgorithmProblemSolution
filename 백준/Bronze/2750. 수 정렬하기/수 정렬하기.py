n = int(input())

x = []

for i in range(n):
    x.append(int(input()))

for i in range(len(x)-1):
    for j in range(len(x)-1,i,-1):
        if x[j-1] > x[j]:
            x[j-1],x[j] = x[j],x[j-1]
            
for i in x:
    print(i)