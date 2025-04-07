from collections import deque
import sys
input =sys.stdin.readline

r,c = map(int,input().split())
graph = [list(map(str, input().strip())) for _ in range(r)]

fire_time = [[-1] * c for _ in range(r)]
jihun_time = [[-1] * c for _ in range(r)]

fire_q = deque()
jihun_q = deque()

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            fire_q.append((i,j))
            fire_time[i][j] = 0
        elif graph[i][j] == 'J':
            jihun_q.append((i,j))
            jihun_time[i][j] = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while fire_q:
    x,y = fire_q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != '#' and fire_time[nx][ny] == -1:
            fire_q.append((nx,ny))
            fire_time[nx][ny] = fire_time[x][y] + 1

while jihun_q:
    x,y = jihun_q.popleft()
    if x == 0 or x == r-1 or y == 0 or y == c-1:
        print(jihun_time[x][y] + 1)
        exit()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != '#' and jihun_time[nx][ny] == -1:
            if fire_time[nx][ny] == -1 or fire_time[nx][ny] > jihun_time[x][y] +1:
                jihun_q.append((nx,ny))
                jihun_time[nx][ny] = jihun_time[x][y] + 1

print("IMPOSSIBLE")