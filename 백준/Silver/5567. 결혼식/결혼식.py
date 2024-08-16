import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    
    while q:
        a = q.popleft()
        
        for i in graph[a]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[a] + 1

bfs(1)
result = 0
for i in visited:
    if i > 1 and i < 4:
        result += 1
        
print(result)