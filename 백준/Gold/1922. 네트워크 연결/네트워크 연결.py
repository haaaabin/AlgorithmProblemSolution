import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = []
parent = [i for i in range(n+1)]

for i in range(m):
   a,b,c = map(int,input().split())
   graph.append((a,b,c))
   
graph.sort(key = lambda x: x[2])

#find함수
def find(x):
   if parent[x] != x:
      parent[x] = find(parent[x])
   return parent[x]

def union(a,b):
   a = find(a)
   b = find(b)

   if a < b:
      parent[b] = a
   else:
      parent[a] = b
      
total_cost = 0
total_edges= 0

for u,v,w in graph:
   if find(u) != find(v):
      union(u,v)
      total_cost +=w
      total_edges +=1
      
      if total_edges == n:
         break
      
print(total_cost)