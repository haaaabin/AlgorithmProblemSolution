from collections import deque
import sys
sys.setrecursionlimit(10**9)

N,M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False] * (N+1)

def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

count = 0
for i in range(1,N+1):
    if not visited[i]:
        dfs(i)    
        count += 1

print(count)