from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(t):
    w,h = map(int,input().split())
    graph = [list(map(str,input().strip())) for _ in range(h)]
    
    fire_time = [[-1] * w for _ in range(h)]
    sanggun_time = [[-1] * w for _ in range(h)]

    fire_q = deque()
    sanggun_q = deque()

    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                fire_time[i][j] = 0
                fire_q.append((i,j))
            elif graph[i][j] == '@':
                sanggun_time[i][j] = 0
                sanggun_q.append((i,j))

    while fire_q:
        x,y = fire_q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if fire_time[nx][ny] == -1 and graph[nx][ny] != '#':
                    fire_time[nx][ny] = fire_time[x][y] +1
                    fire_q.append((nx,ny))

    escaped = False
    while sanggun_q:
        x,y = sanggun_q.popleft()

        if x == 0 or x == h-1 or y == 0 or y == w-1:
            print(sanggun_time[x][y] + 1)
            escaped = True
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if  0 <= nx < h and 0 <= ny < w:
                if sanggun_time[nx][ny] == -1 and graph[nx][ny] != '#':
                    if fire_time[nx][ny] == -1 or fire_time[nx][ny] > sanggun_time[x][y] + 1:
                        sanggun_time[nx][ny] = sanggun_time[x][y] + 1
                        sanggun_q.append((nx,ny))

    if not escaped:
        print("IMPOSSIBLE")
