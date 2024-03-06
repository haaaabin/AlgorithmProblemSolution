import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]

    q = deque()
    q.append([x,y])
    islands[x][y] = 0
    
    while q:
        a,b =q.popleft()
        
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w and islands[nx][ny] == 1:
                islands[nx][ny] = 0
                q.append([nx,ny])


while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
       break
    
    islands = []
    cnt = 0
    for i in range(h):
        islands.append(list(map(int, input().split()))) 
    
    for i in range(h):
        for j in range(w):
            if islands[i][j] ==1:
                bfs(i,j)
                cnt +=1
                
    print(cnt)