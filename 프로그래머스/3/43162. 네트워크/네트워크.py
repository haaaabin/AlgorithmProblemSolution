from collections import deque

def solution(n, computers):
    visited = [False] * n
    
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            for i in range(n):
                if computers[node][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)
    
    count = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            count += 1
            
    return count
