import sys
input = sys.stdin.readline

n = int(input())

table = []

for i in range(n):
    start, end = map(int,input().split())
    table.append((start,end))
    
table.sort(key = lambda x: (x[1], x[0]))

last_end_time = 0
cnt = 0

for s, e in table:
    if s >= last_end_time:
        cnt +=1
        last_end_time = e

print(cnt)