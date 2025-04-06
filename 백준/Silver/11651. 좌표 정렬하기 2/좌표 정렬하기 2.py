import sys
input = sys.stdin.readline

N = int(input())
temp = []
for _ in range(N):
    x,y = map(int, input().split())
    temp.append((x,y))

temp.sort(key=lambda x:(x[1],x[0]))

for t in temp:
    print(t[0], t[1])