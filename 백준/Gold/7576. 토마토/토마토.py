import sys
from collections import deque

M , N = map(int,input().split())
tomatos = []
for _ in range(N):
    tomatos.append(list(map(int,input().split())))

dx = [-1,1,0,0,]
dy = [0,0,-1,1]
       
def bfs():
    q = deque([])
    
    for i in range(N):
        for j in range(M):
            if tomatos[i][j] == 1:
                q.append([i,j])

    while q:
        x , y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and tomatos[nx][ny] == 0:
                tomatos[nx][ny] = tomatos[x][y] + 1
                q.append([nx,ny])
       
bfs()      
     
day = 0
for row in tomatos:
    for toma in row:
        if toma == 0:
            print(-1)
            exit()
    day = max(day, max(row))
    
print(day - 1)