import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N,M = map(int,input().split())
graph = [list(input().strip()) for _ in range(M)]

def bfs(x,y,color):
    q = deque()
    q.append((x,y))
    graph[x][y] = '.'
    cnt = 1

    while q:
        x_, y_ = q.popleft()

        for i in range(4):
            nx = x_ + dx[i]
            ny = y_ + dy[i]

            if (0 <= nx < M and 0 <= ny < N and graph[nx][ny] == color):
                q.append((nx,ny))
                graph[nx][ny] = '.'
                cnt += 1

    return cnt

W_result = 0
B_result = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 'W':
            W_result += bfs(i,j,'W') **2
        elif graph[i][j] == 'B':
            B_result += bfs(i,j,'B') **2

print(W_result, B_result)