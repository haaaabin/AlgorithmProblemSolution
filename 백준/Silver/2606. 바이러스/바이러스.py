from collections import deque
import sys

n = int(sys.stdin.readline())
v = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]

for i in range(v):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited=[False] * (n+1)
    
def bfs(x):
    q =deque()
    q.append(x)
    
    visited[x] = True
    count =0
    while q:
        a = q.popleft()
        
        for i in graph[a]:
            if not visited[i]:
                q.append(i)
                visited[i]= True 
                count +=1
    return count
print(bfs(1))