import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

cities = [[] for _ in range(n+1)]

#최단거리
distance = [INF] * (n+1)

for i in range(m):
    u, v, w = map(int,input().split())
    cities[u].append((w,v))

start, end = map(int,input().split())

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    
    while q:
        dist, next = heapq.heappop(q)
        
        #현재 노드가 처리된 적이 있으면?
        if distance[next] < dist:
            continue
        
        for nx in cities[next]:
            cost = dist + nx[0]
            if distance[nx[1]] > cost:
                distance[nx[1]] = cost
                heapq.heappush(q, (cost,nx[1]))
                             

dijkstra(start)

print(distance[end])