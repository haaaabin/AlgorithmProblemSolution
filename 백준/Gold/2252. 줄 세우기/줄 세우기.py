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
    
def toplogy_sort():
    q = deque()
    result = []
    #진입 차수 0인 노드 큐에 추가
    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        p = q.popleft()
        result.append(p)
        for i in student[p]:
            indegree[i] -=1
            if indegree[i] == 0:
                q.append(i)
                
    for res in result:
        print(res, end=" ")    
        
toplogy_sort()