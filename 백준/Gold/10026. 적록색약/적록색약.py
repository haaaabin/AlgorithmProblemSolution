import sys
from collections import deque
input = sys.stdin.readline


def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited_bfs[x][y] = 1
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while q:
        x_,y_= q.popleft()
        
        for i in range(4):
            nx = x_ + dx[i]
            ny = y_ + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == graph[x][y] and not visited_bfs[nx][ny]:
                q.append((nx,ny))
                visited_bfs[nx][ny] = 1

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited_bfs = [[0] * n for _ in range(n)]

cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited_bfs[i][j]:
            bfs(i,j)
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited_bfs = [[0] * n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited_bfs[i][j]:
            bfs(i,j)
            cnt2 += 1
            
print(cnt1,cnt2)  