from collections import deque
import sys

# 정점의 개수 n , 간선의 개수 m , 탐색을 시작할 정점의 번호 v
n,m,v = map(int,sys.stdin.readline().split())

# 그래프 생성  
graph = [[0] * (n+1) for _ in range(n+1)]

# 인접 행렬로 무방향 그래프
for i in range(m):
    n1, n2 = map(int,sys.stdin.readline().split())
    graph[n1][n2] = 1   #무방향 그래프
    graph[n2][n1] = 1
    
#방문 체크할 리스트
visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)

#깊이 탐색
def dfs(v):
    visited_dfs[v] = 1
    print(v, end =" ")
    
    for i in range(1,n+1):
        if graph[v][i]==1 and visited_dfs[i] == 0:
            dfs(i)

#너비 탐색, 큐
def bfs(v):
    #큐 생성 , 큐에 시작 노드 삽입
    q = deque()
    q.append(v)
    
    # 큐에 넣고 방문처리를 해야 함
    visited_bfs[v] = 1
    
    #아직 방문해야 하는 노드가 있다면
    while q:
        #큐에서 노드를 꺼내 x에 저장
        x = q.popleft()
        print(x, end =" ")

        for i in range(1,n+1):
            # 그래프를 탐색하다가 방문하지 않은 노드가 있고 연결되어있다면
            if graph[x][i] == 1 and visited_bfs[i]== 0:
                #큐에 삽입하고 방문 처리
                q.append(i)
                visited_bfs[i] = 1

                      
dfs(v)
print()
bfs(v)