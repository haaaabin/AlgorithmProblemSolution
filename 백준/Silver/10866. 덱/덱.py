import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

deq = deque()
for i in range(N):
    comment = list(input().split())
    
    if comment[0] == "push_front":
        deq.appendleft(comment[1])
    elif comment[0] == "push_back":
        deq.append(comment[1])
    elif comment[0] == "pop_front":
        if len(deq) != 0:
            print(deq.popleft())
        else:
            print(-1)
    elif comment[0] == "pop_back":
        if len(deq) != 0:
            print(deq.pop())
        else:
            print(-1)
    elif comment[0] == "front":
        if len(deq) != 0:
            print(deq[0])
        else:
            print(-1)
    elif comment[0] =="size":
        print(len(deq))
    elif comment[0] == "empty":
        if len(deq) != 0:
            print(0)
        else:
            print(1)
    elif comment[0] == "back":
        if len(deq) != 0:
            print(deq[-1])
        else:
            print(-1)