import sys
input = sys.stdin.readline

S = input().strip()
lst = list(S)

temp = []

while lst:
    temp.append(''.join(lst))
    lst = lst[1:]

temp.sort(key = lambda x:x)
for t in temp:
    print(t)