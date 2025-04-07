n = int(input())
ropes = [int(input()) for _ in range(n)]

ropes.sort()

max_weight = 0

for i in range(n):
    weight = ropes[i] * (n-i)
    max_weight = max(weight, max_weight)

print(max_weight)