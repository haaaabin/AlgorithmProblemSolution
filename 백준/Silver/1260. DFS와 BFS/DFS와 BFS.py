import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int,input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
visited_bfs = [False] * (n+1)
visited_dfs = [False] * (n+1)

for i in range(m):
    n1, n2 = map(int,input().split())
    graph[n1][n2] = 1
    graph[n2][n1] = 1

def bfs(x):
    q = deque()
    q.append(x)
    visited_bfs[x] = True
    
    while q:
        a = q.popleft()
        print(a, end=" ")
        for i in range(1, n+1):
            if graph[a][i] == 1 and not visited_bfs[i]:
                q.append(i)
                visited_bfs[i]= True

def dfs(x):
    visited_dfs[x] = True
    print(x, end= " ")
    
    for i in range(1, n+1):
        if graph[x][i] == 1 and not visited_dfs[i]:
             dfs(i)
dfs(v)
print()
bfs(v) 