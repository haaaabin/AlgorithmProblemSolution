import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

q = deque()
for i in range(N):
    comment = list(input().split())
    
    if comment[0] == "push":
        q.append(comment[1])
    elif comment[0] == "pop":
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)
    elif comment[0] == "front":
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    elif comment[0] =="size":
        print(len(q))
    elif comment[0] == "empty":
        if len(q) != 0:
            print(0)
        else:
            print(1)
    elif comment[0] == "back":
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)