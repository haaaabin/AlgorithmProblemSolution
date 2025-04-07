from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    cnt = 1

    while q:
        x,y, = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and graph[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx,ny))
                cnt += 1
    
    return cnt

count = 0
size = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] == False and graph[i][j] == 1:
            count += 1
            size = max(size , bfs(i, j))

print(count)
print(size)