N = int(input())

temp = [int(input()) for _ in range(N)]
temp.sort()
for i in temp:
    print(i)