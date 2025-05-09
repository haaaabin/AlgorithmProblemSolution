from collections import deque
import sys
input = sys.stdin.readline

m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((i,j))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

bfs()

day = 0
for row in graph:
    for i in row:
        if i == 0:
            print(-1)
            exit()
    day = max(day, max(row))

print(day-1)