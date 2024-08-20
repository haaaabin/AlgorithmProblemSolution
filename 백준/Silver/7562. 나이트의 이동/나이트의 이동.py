import sys
from collections import deque
input = sys.stdin.readline

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [-2,-1,1,2,-2,-1,1,2]

def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        xx,yy = q.popleft()

        if xx == end_x and yy == end_y:
           print(graph[xx][yy])
           break
        
        for i in range(8):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0 <= nx < I and 0 <= ny < I and graph[nx][ny] == 0:
                q.append((nx,ny))
                graph[nx][ny] = graph[xx][yy] + 1
    
t = int(input())
for i in range(t):
    I = int(input())
    graph = [[0] * I for _ in range(I)]
    start_x,start_y = map(int,input().split())
    end_x , end_y = map(int,input().split())

    bfs(start_x,start_y)
