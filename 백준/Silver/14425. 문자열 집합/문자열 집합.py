n, m = map(int, input().split())

s = [input() for _ in range(n)]
temp = [input() for _ in range(m)]

s.sort()
temp.sort()

count = 0
for i in temp:
    if i in s:
        count += 1

print(count)