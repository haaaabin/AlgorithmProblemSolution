import sys, heapq
input = sys.stdin.readline

n,m = map(int,input().split())

houses = []
parent = [i for i in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    houses.append((a,b,c))
    
houses.sort(key= lambda x:x[2])

def find(x):
    if parent[x] != x:
        x = find(parent[x])
    return parent[x]

def union(_x,_y):
    _x = find(_x)
    _y = find(_y)
    
    if _x < _y:
        parent[_y] = _x
    else:
        parent[_x] = _y
        
total_cost = 0
max = 0

for u,v,w in houses:
    if find(u) != find(v):
        union(u,v)
        total_cost += w
        max = w

print(total_cost - max)