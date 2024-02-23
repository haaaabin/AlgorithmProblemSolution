import sys
input = sys.stdin.readline

n,m = map(int,input().split())

nonlisten = []
nonsee = []

for i in range(n):
    nonlisten.append(input().rstrip())
for i in range(m):
    nonsee.append(input().rstrip())
    
answer = list(set(nonlisten) & set(nonsee))
answer.sort()

print(len(answer))
for a in answer:
    print(a)