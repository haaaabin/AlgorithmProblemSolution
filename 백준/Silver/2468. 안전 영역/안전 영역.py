from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
max_height = max(map(max,graph))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,h):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n  and graph[nx][ny] > h and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True

max_area = 0
for h in range(0, max_height+1):
    visited = [[False] * n for _ in range(n)]
    count = 0 
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h:
                bfs(i,j,h)
                count += 1
                
    max_area = max(max_area, count)

print(max_area)