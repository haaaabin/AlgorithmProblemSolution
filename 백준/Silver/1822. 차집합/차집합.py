import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = set(map(int,input().split()))
b = set(map(int,input().split()))

result = sorted(a.difference(b))

if result:
    print(len(result))
    print(*result)
else:
    print(0)