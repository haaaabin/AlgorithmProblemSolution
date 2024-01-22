import heapq
import sys

v,e = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(v+1)]

#인접 리스트
for _ in range(e):
    u,vertex,w = map(int,sys.stdin.readline().split())
    graph[u].append([w,vertex])  
    graph[vertex].append([w,u])
    
#방문 처리
visited = [False] * (v+1)

def prim(x):
    #시작 노드 방문 체크
    visited[x] = True
    #가중치가 최소인 간선을 선택하기 위한 최소힙(우선순위큐)
    heap = graph[x]
    #우선순위큐로 만듬
    heapq.heapify(heap)
    total_cost = 0

    while heap:
        weight, n = heapq.heappop(heap)
        
        if not visited[n]:
            #방문하지 않은 노드인 경우 방문처리
            visited[n] = True
            total_cost += weight
            
            for w,u in graph[n]:
                if not visited[u]:
                    #아직 방문하지 않은 노드만 최소힙에 넣음
                    heapq.heappush(heap,[w,u])
    return total_cost

print(prim(1))