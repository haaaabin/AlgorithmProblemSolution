import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())

temp = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    temp[a].append((c,b))
    temp[b].append((c,a))
    
def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0,start))
    distance[start] = 0
    
    while heap:
        dist, now = heapq.heappop(heap)
        
        if distance[now] < dist:
            continue
        
        for next_dist, next_node in temp[now]:
            total_cost = dist + next_dist
            if total_cost < distance[next_node]:
                distance[next_node] = total_cost
                heapq.heappush(heap, (total_cost, next_node))
                
    return distance[n]

print(dijkstra(1))