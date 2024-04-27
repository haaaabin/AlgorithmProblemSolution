import sys
from collections import deque
input = sys.stdin.readline

M,N,K = map(int,input().split())
graph = [[0] * (N) for _ in range(M)]
for _ in range(K):
    x1,y1,x2,y2= map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):        
    q = deque()
    q.append([x,y])
    area = 1
    
    while q:
        b, a = q.popleft()
        for i in range(4):
            nx = a + dx[i] 
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                q.append([ny,nx])
                area += 1
    return area

res = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = 1
            res.append(bfs(i,j))

print(len(res))
print(*sorted(res))