import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0     #자기 자신의 비용은 0으로 초기화
            
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(c, graph[a][b])   #시작 노드와 도착 도시를 연결하는 노선은 하나가 아닐 수도 있다.
    
for a in range(1,n+1):
    for b in range(1, n+1):
        for c in range(1,n+1):
            graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c])
            
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end =' ')
        else:
            print(graph[i][j], end =' ')
    print()