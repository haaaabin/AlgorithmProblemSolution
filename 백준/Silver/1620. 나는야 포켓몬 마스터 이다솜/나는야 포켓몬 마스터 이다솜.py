import sys
input = sys.stdin.readline

N,M =map(int,input().split())

poketmon = {}

for i in range(1,N+1):
    name = input().rstrip()
    poketmon[i] = name
    poketmon[name] = i
    
for i in range(M):
    quest = input().rstrip()

    if quest.isdigit():
        print(poketmon[int(quest)])
    else:
        print(poketmon[quest])