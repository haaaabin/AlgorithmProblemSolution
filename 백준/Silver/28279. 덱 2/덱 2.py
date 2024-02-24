import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

deq = deque()
for i in range(N):
    command = list(map(int,input().split()))
    if command[0] == 1:
        deq.appendleft(command[1])
    elif command[0] == 2:
        deq.append(command[1])
    elif command[0] == 3:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif command[0] == 4:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif command[0] == 5:
        print(len(deq))
    elif command[0] == 6:
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 7:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif command[0] == 8:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])