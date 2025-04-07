from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx,ny))

for _ in range(T):
    m,n,k = map(int,input().split())
    graph = [[0] * n for _ in range(m)]
    visited = [[0] * n for _ in range(m)]

    for _ in range(k):
        x,y= map(int,input().split())
        graph[x][y]=1

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                cnt += 1
    print(cnt)