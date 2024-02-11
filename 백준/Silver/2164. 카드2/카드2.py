from collections import deque
import sys
input = sys.stdin.readline

N= int(input())

q = deque([i for i in range(1,N+1)])

while True:
    if len(q) == 1:
        print(q.popleft())
        break
    else:      
        q.popleft()
        q.append(q.popleft())