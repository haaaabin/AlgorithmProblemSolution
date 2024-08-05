import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited_dfs = [0] * (N+1)
cnt = 1

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()

def dfs(x):
    global cnt
    visited_dfs[x] = cnt

    for i in graph[x]:
        if visited_dfs[i] == 0:
            cnt += 1
            dfs(i)

dfs(R)

for i in visited_dfs[1:]:
    print(i)