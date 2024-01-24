import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())

trees=[[] for _ in range(n+1)]

for i in range(n-1):
    n1, n2 = map(int,input().split())
    trees[n1].append(n2)
    trees[n2].append(n1)
    
visited = [False] * (n+1)

def dfs(start):
    
    for tree in trees[start]:
        if not visited[tree]:
            visited[tree] = start
            dfs(tree)
                
dfs(1)

for x in range(2,n+1):
    print(visited[x])