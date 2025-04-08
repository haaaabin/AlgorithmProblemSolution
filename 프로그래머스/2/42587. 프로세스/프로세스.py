from collections import deque

def solution(priorities, location):
    answer = 0
    process = deque([(p,i) for i, p in enumerate(priorities)])
    
    while process:
        q = process.popleft()
        
        if any(q[0] < p[0] for p in process):
            process.append(q)
        else:
            answer += 1
            
            if q[1] == location:
                return answer