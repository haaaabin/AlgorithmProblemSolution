def fac(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * fac(n-1)

n = int(input())
temp = list(str(fac(n)))
cnt = 0

for i in range(len(temp)-1,-1,-1):
    if temp[i] == '0':
        cnt +=1
    else:
        break
        
print(cnt)