import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
peoples = [list(input().rstrip()) for _ in range(M)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b,color):
    q = deque()
    q.append((a,b))
    cnt = 1
    peoples[a][b]= "."
    while q:
        x, y  = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(0 <= nx < M and 0 <= ny < N and peoples[nx][ny] == color):
                peoples[nx][ny] = "."
                q.append((nx,ny))
                cnt += 1
    return cnt    

w_result = 0
b_result = 0
for i in range(M):
    for j in range(N):
        if peoples[i][j] == "W":
            w_result += bfs(i,j,"W") **2
        elif peoples[i][j] == "B":
            b_result += bfs(i,j,"B") **2 
            
print(w_result, b_result)