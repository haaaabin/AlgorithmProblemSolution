from collections import deque
import sys

N,M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False] * (N+1)


def bfs(x):
    q =deque()
    q.append(x)

    visited[x] = True
    
    while q:
        a = q.popleft()       
        for i in graph[a]:
            if not visited[i]:
                q.append(i)
                visited[i]= True
            
count = 0
for i in range(1,N+1):
    if not visited[i]:
        bfs(i)          #bfs를 실행하면 count + 1 -> bfs를 실행하는 횟수가 연결요소의 개수
        count += 1

print(count)