# 정점, 간선 갯수 받아옴
v, e = map(int,input().split())

#부모 노드를 자기 자신으로 초기화
parent = [i for i in range(v+1)]    

graph = []
for _ in range(e):
    a,b,c = map(int,input().split())
    graph.append((a,b,c))   #튜플로 묶어서 추가

#가중치 오름차순으로 정렬
graph.sort(key = lambda x:x[2])

# find
def find(x):
    #만약 x의 부모가 자기자신이 아니라면 재귀를 통해 루트 노드를 찾는다.
    if parent[x] != x:
        parent[x] = find(parent[x])
    #자기 자신이면 본인이 루트노드인 경우이므로 그대로 출력한다.
    return parent[x]
    
# union
def union(a,b):
    #a와 b의 루트노드 찾기
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#가중치 합
total_cost = 0 

for u,v,w in graph:
    if find(u) != find(v):
        union(u,v)
        total_cost += w
        
print(total_cost)