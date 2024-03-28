import sys
input = sys.stdin.readline

N = int(input())
people = []
rank = [1] * N
for _ in range(N):
    x,y = map(int,input().split())
    people.append((x,y))
    
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] +=1

for r in rank:
    print(r, end=" ")