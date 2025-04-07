import sys
input = sys.stdin.readline

N = int(input())

temp = []
for _ in range(N):
    name , korean, english, math = map(str ,input().split())
    temp.append((name, int(korean), int(english), int(math)))

temp.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for t in temp:
    print(t[0])