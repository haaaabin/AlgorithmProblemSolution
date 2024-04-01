import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    q = deque()
    q.append(n)
    
    while q:        # 처음 시작점은 cur = 5
        cur = q.popleft()
        if(cur == K):
            print(dist[cur])
            break
        for nx in (cur-1, cur+1, cur*2):    #nx = 4, 6, 10
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[cur] + 1
                q.append(nx)
                
N, K = map(int,input().split())
MAX = 10**5
dist = [0] * (MAX+1)

bfs(N)