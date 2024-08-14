import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N,M,K = map(int,input().split())
graph = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for _ in range(K):
    r,c = map(int,input().split())
    graph[r-1][c-1] = 1

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    cnt = 1

    while q:
        x_ , y_ = q.popleft()

        for i in range(4):
            nx = x_ + dx[i]
            ny = y_ + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1 and not visited[nx][ny] :
                q.append((nx,ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt

res = 1
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            res = max(res, bfs(i,j))
print(res)