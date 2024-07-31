import sys
from collections import deque
input = sys.stdin.readline

N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited_bfs = [0] * (N+1)
cnt = 1

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort(reverse=True)

def bfs(x):
    q = deque()
    q.append(x)
    global cnt 
    visited_bfs[x] = cnt
    
    while q:
        x_ = q.popleft() 

        for i in graph[x_]:
            if visited_bfs[i] == 0:
                q.append(i)
                cnt += 1
                visited_bfs[i] = cnt

bfs(R)
for i in visited_bfs[1:]:
    print(i)