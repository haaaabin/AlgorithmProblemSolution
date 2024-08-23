from collections import deque

a,b = map(int,input().split())

q = deque()
q.append((a,1))

while q:
    x, c = q.popleft()
    if x == b:
        print(c)
        exit()
    
    if x*2 <= b:
        q.append((x*2, c+1))
    
    x = int(str(x) + "1")  
    if x <= b:
        q.append((x,c+1))

print(-1)