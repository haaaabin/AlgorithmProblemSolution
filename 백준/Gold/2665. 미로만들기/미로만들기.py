import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

miro = []

for _ in range(n):
    miro.append(list(map(int,input().rstrip())))

#검은 방을 흰 방으로 바꾼 횟수
visited = [[-1]* n for _ in range(n)] 

    #하 우 상 좌
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0]=0
    
    while q:
        x,y = q.popleft()
        if x == n-1 and y == n-1:
            return visited[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                # 해당 위치가 흰 방(1)이면
                if miro[nx][ny] ==1:
                    #흰 방 먼저 탐색
                    q.appendleft((nx,ny))
                    #이전 visited의 값을 초기화
                    visited[nx][ny] = visited[x][y]
                else:
                    q.append((nx,ny))
                    #이전 visited에서 1을 더해서 초기화
                    visited[nx][ny] = visited[x][y]+1
                    
print(bfs())   