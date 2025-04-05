T = int(input())

for _ in range(T):        
    temp = {}
    n = int(input())
    for i in range(n):
        name, kind = input().split()
        if kind in temp.keys():
            temp[kind] += [name]
        else:
            temp[kind] = [name]

    answer = 1
    for value in temp.values():
        answer *= (len(value) + 1)
    print(answer - 1)