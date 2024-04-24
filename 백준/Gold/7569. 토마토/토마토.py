import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
q = deque([])

def bfs():
    while q:
        z,x,y = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]     
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                q.append((nz,nx,ny))
                
M,N,H = map(int,input().split())
graph = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                q.append((i,j,k)) 
bfs()
                
day = 0
for i in graph:
    for j in i:
        if 0 in j:
            print(-1)
            exit(0)
        day = max(day, max(j))
print(day - 1) 