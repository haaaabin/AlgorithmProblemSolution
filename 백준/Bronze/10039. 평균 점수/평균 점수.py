temp = []
for _ in range(5):
    n = int(input())
    temp.append(n)

sum = 0
for i in temp:
    if i < 40:
        i = 40
    sum += i

average = sum / 5

print(int(average))