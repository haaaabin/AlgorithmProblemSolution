n,k = map(int,input().split())

lans = []
for i in range(n):
    lans.append(int(input()))

s = 1          
e = max(lans)

while s <= e:
    mid = (s+e) //2
    LAN = 0
    
    for i in lans:
        LAN += i // mid
    
    if LAN >= k:
        s = mid + 1
    else:
        e = mid - 1
        
print(e)