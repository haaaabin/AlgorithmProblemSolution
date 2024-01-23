import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

#도시의 개수 n, 도로의 개수 m, 거리 정보 k, 출발 도시 번호 x
n,m,k,x = map(int, input().split())

graph=[[] for _ in range(n+1)]

#최단 거리 테이블을 모두 INF로 초기화
distance = [INF] * (n+1)

for i in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append((1,n2))
    
def dijkstra(start):
    q =[]
    distance[start] = 0             #시작 노드 최단 경로 0
    heapq.heappush(q,(0,start))     
    
    while q:
        dist, now = heapq.heappop(q)    
        
        # 현재 노드가 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for next in graph[now]:
            cost = dist + next[0]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[next[1]] > cost:
                distance[next[1]] = cost
                heapq.heappush(q,(cost,next[1]))
                
dijkstra(x)
#최단 거리 k인 모든 도시 담아줄 리스트
result =[]

for i in range(1,n+1):
    if distance[i]==k:
        result.append(i)

# 최단 거리가 K인 도시가 하나도 존재하지 않으면 
if len(result) == 0:
    print(-1)

for res in result:
    print(res, end="\n")