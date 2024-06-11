import sys
input = sys.stdin.readline

N = int(input())
temp = []
for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    temp.append((age, name))

temp.sort(key = lambda x : x[0])

for i in temp:
    print(i[0], i[1])