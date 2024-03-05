from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0,-1, 0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    baechu[x][y] = 0
    
    while q:
        x_ , y_ = q.popleft()

        for i in range(4):
            nx = x_ + dx[i]
            ny = y_ + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M or baechu[nx][ny] == 0:
                continue
            
            if baechu[nx][ny] ==1:
                q.append((nx,ny))
                baechu[nx][ny] = 0
     
T = int(input())
for _ in range(T):
    N,M,K = map(int,input().split())
    baechu = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        x,y = map(int,input().split())
        baechu[x][y] = 1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if baechu[i][j] == 1:
                  bfs(i,j)
                  cnt +=1
    print(cnt) 