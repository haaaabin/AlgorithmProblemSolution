m,n = map(int,input().split())
snacks = list(map(int,input().split()))

start = 1
end = max(snacks)

while start <= end:
    mid = (start+end) // 2
    count = 0
    
    for snack in snacks:
        count += snack // mid
        if count >= m:
            break
    
    if count < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)