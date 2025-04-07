from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

graph = [list(map(int,input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    cnt = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
                cnt += 1

    return cnt

houses = []
count = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            houses.append(bfs(i,j))
            count += 1

print(count)

houses.sort()
for house in houses:
    print(house)