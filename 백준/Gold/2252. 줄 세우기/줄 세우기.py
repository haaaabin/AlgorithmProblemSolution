from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

student = [[] for _ in range(N+1)]

indegree = [0] * (N+1)

for i in range(M):
    a,b = map(int,input().split())
    student[a].append(b)
    indegree[b] +=1
    
q = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        
while q:
    p = q.popleft()
    print(p, end =" ")
    
    for i in student[p]:
        indegree[i] -=1
        if indegree[i] == 0:
            q.append(i)