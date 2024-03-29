import sys
input = sys.stdin.readline

N = int(input())
temp= []

for i in range(N):
    temp.append(list(map(int,input().split())))

temp.sort(key = lambda x: (x[0],x[1]))

for i in temp:
    print(i[0], i[1])