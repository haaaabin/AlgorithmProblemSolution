temp = [int(input()) for _ in range(10)]

na_temp = []
for i in temp:
    na = i % 42
    na_temp.append(na)

print(len(set(na_temp)))