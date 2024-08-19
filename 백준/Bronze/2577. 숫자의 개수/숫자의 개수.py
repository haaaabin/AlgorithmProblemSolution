a = int(input())
b = int(input())
c = int(input())

mul = list(str(a*b*c))
temp = [0 for _ in range(10)]
for i in range(10):
    for n in mul:
        if str(i) == n:
            temp[i] += 1

for a in temp:
    print(a)