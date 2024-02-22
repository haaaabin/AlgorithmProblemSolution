import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(node, cnt):
    vistied[node] = True
    
    for nodes in graph[node]:
        if vistied[nodes] ==False:
            cnt = dfs(nodes, cnt +1) 
    return cnt

T = int(input())

for i in range(T):
    N,M = map(int,input().split())
    graph = [[] for i in range(N+10)]
    vistied = [False] * (N+1)
    
    for i in range(M):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
           
    print(dfs(1,0))