import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

miro = []

for _ in range(n):
    miro.append(list(map(int,sys.stdin.readline().rstrip())))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
   
def bfs(x,y):
    q=deque()
    q.append((x,y))
    
    while q:
        x, y = q.popleft()
        #상 하 좌 우 검사
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0  or ny >=m or miro[nx][ny] == 0:
                continue
            
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                q.append((nx,ny))
            
    return miro[n-1][m-1]

print(bfs(0,0))