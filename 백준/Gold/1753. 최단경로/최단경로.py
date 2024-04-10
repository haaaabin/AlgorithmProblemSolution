import sys , heapq
input = sys.stdin.readline
INF = sys.maxsize

v,e = map(int,input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
visited = [INF] *(v+1)

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    heap = []
    visited[start] = 0
    heapq.heappush(heap, (0,start))
    total_weight = 0
    
    while heap:
        weight, node = heapq.heappop(heap)
        
        if visited[node] < weight:
            continue
        
        for next_node, next_weight in graph[node]:
            total_weight = weight + next_weight
            
            if total_weight < visited[next_node]:
                visited[next_node] = total_weight
                heapq.heappush(heap, (total_weight, next_node))
                
dijkstra(k)

for i in range(1, v+1):
    if visited[i] == INF:
        print("INF")
    else:
        print(visited[i])